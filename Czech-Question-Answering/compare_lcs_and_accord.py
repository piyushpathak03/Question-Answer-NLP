# Recompute start index, end index and match of the translated answer in the translated text from the *inputfile* and store results into *outputfile*.
import multiprocessing.pool
import json
import sys
import string

inputfile = sys.argv[1] 
outputfile = sys.argv[2]
threads = int(sys.argv[3]) if len(sys.argv) > 3 else 1

# class for storing information about subsequences
class Subsequence:
    def __init__(self, match_value, start_index, end_index):
        self.match_value = match_value
        self.start_index = start_index
        self.end_index = end_index

# iterate in text char by char and find lcs in the substring of the text of the certain window_size 
def iterate_text(params):
    text, answer, middle_orig_index = params

    # dictionary for the subsequences with the same match value
    subs_list = []
    match_max = 0 
    # iterare text window by window and in each find lcs
    for i in range(0,len(text)):
        if (i==0 or text[i-1].isspace() or text[i-1] in string.punctuation) and not text[i].isspace():
            s = lcs(text[i:len(text)], answer,i)
            s.start_index += i
            s.end_index += i
    
            # if another longest lcs with the same length as existing one found append it to the list
            if s.match_value==match_max:            
                subs_list.append(s)
               
            # if the new longest lcs found create new list and update match_max
            elif s.match_value>match_max:
                subs_list.clear()
                subs_list.append(s)
                match_max = s.match_value        
     
    best = subs_list[0]
    max_accord = 0
    s = subs_list[0]

    # recompute match according to the position in the text and original position of the answer before translating
    for i in range(0,len(subs_list)):
        s = subs_list[i]
        middle_act_index = (s.end_index+s.start_index)/2
        position_match = s.match_value*(1-abs(middle_orig_index/len(text)-middle_act_index/len(text)))
        # find the answer position with highest accord
        if position_match > max_accord:
            max_accord = position_match
            best = s  
    return best
        
# find longest common substring of context and answer and return answer start and end index and matching value
def lcs(text, answer,idx):  
    rows = len(text) +1
    cols = len(answer) +1
    # create empty array of size rows*cols
    array_matches = [[0 for i in range(cols)] for j in range(rows)]
    
    # define values for the best matching subsrting
    match_idx_i = 0
    match_idx_j = 0
    match_value = 0
    ii = 0
    
    # fill the matrix with lenghts of longest subsequences
    for i in range(1, rows):       
        for j in range(1, cols):
            # if the chars match, go for left-top diagonal value + 1
            if text[i - 1] == answer[j - 1]:
                array_matches[i][j] = array_matches[i - 1][j - 1] + 1
            # otherwise get max of top or left
            else:
                array_matches[i][j] = max(array_matches[i - 1][j], array_matches[i][j - 1])             
            # compute matching value with respect to length to the subsequence
            act_match = 2*array_matches[i][j]/(i+len(answer))            
            if (i + 1 == rows or text[i].isspace() or text[i] in string.punctuation) and not text[i-1].isspace():
                if act_match > match_value:             
                    match_idx_i = i
                    match_idx_j = j
                    match_value = act_match 
                    ii = i
   
    end_index = match_idx_i-1 
    match_value = 2*array_matches[match_idx_i][match_idx_j]/(ii+len(answer))
    s = Subsequence(match_value, 0, end_index)
    return s

#load input json file
def load_file(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file) 
    print('--DATA SUCCESSFULLY LOADED--')
    return data

# save data to json file
def save_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False)
    print('--DATA SUCCESSFULLY SAVED--')    
    
def main():
    data = load_file(inputfile)
    
    queue = []

    def correct_lower(text):
        text_lower = text.replace("İ", "i").lower()
        assert len(text_lower) == len(text)
        return text_lower

    # iterate and translate topic by topic
    for i in range(0, len(data['data'])):        
        # iterate and translate paragraph by paragraph
        for j in range(0, len(data['data'][i]['paragraphs'])):
            translated_context = correct_lower(data['data'][i]['paragraphs'][j]['context'])
            # iterate and translate question by question
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):             
                # iterate and translate answer by answer
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):                 
                    translated_answer = correct_lower(data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'])
                    idx =  data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] 
                    queue.append((translated_context, translated_answer, idx))

    results = multiprocessing.pool.Pool(threads).imap(iterate_text, queue)

    processed, text_changed, match_changed = 0, 0, 0
    # iterate and translate topic by topic
    for i in range(0, len(data['data'])):        
        print("Data", i, len(data['data']), file=sys.stderr, flush=True)
        # iterate and translate paragraph by paragraph
        for j in range(0, len(data['data'][i]['paragraphs'])):
            # iterate and translate question by question
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):             
                # iterate and translate answer by answer
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):                 
                    best_answer = next(results)
                    if data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_match'] != best_answer.match_value:
                        match_changed += 1

                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] = best_answer.start_index
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_end'] = best_answer.end_index
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_match'] = best_answer.match_value
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text_translated'] = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'] = data['data'][i]['paragraphs'][j]['context'][best_answer.start_index : best_answer.end_index + 1]

                    processed += 1
                    if data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text_translated'] != data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']:
                        text_changed += 1

        print(processed, text_changed, match_changed, file=sys.stderr)
    print("--SUCCESSFULLY RECOMPUTED START INDEX OF NEW ANSWER--")
    save_file(data, outputfile)     

if __name__ == "__main__":
    main()
    








