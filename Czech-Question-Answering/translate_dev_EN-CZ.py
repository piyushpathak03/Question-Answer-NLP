# translate text in english in inputfile using lindat translator and store output in czech to outputfile
import json
import sys
import requests

inputfile = sys.argv[1] #'data/testsmall'
outputfile = sys.argv[2] #'data/translatedTest'

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

# translate text by using LINDAT transaltion from English to Czech
def translate(text):
    url = "https://lindat.mff.cuni.cz/services/transformer/api/v2/models/en-cs?src=en&tgt=cs" # Set destination URL here
    header = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain", 'charset':'utf-8'}
    data = { "input_text":text }
    request = requests.post(url, headers = header, data=data)
    request.encoding = 'utf-8'
    r = request.text.rstrip()
    return r

def main():
    data = load_file(inputfile)
    
    # iterate and translate topic by topic
    for i in range(0, len(data['data'])):
        text = data['data'][i]['title']  
        translated_topic = translate(text)
        data['data'][i]['title'] = translated_topic  
         
        # iterate and translate paragraph by paragraph
        for j in range(0, len(data['data'][i]['paragraphs'])):
            text = data['data'][i]['paragraphs'][j]['context']
            translated_context = translate(text)
            data['data'][i]['paragraphs'][j]['context'] = translated_context  
            
            # iterate and translate question by question
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):
                text = data['data'][i]['paragraphs'][j]['qas'][k]['question']
                translated_question = translate(text)
                data['data'][i]['paragraphs'][j]['qas'][k]['question'] = translated_question
                
                # iterate and translate answer by answer
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):                 
                    text = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']  
                    translated_answer = translate(text)
                    data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'] = translated_answer                  
                    
    print('--TRANSLATION FINISHED--') 
    save_file(data, outputfile)

if __name__ == "__main__":
    main()
    
 
                
