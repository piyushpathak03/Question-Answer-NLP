# Lemmatize answers in *inputfile* with development dataset using MorphoDita and save the results to the *outputfile*
# Lemmatize model can be extracted from http://hdl.handle.net/11234/1-1836
import json
import sys
import xml.etree.ElementTree as ET

import lemmatizer

inputfile = 'dev-90.json'
outputfile = 'dev-90-lemmatized.json'

# load input json file
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

    for i in range(0, len(data['data'])):
        for j in range(0, len(data['data'][i]['paragraphs'])):           
            for k in range(0, len(data['data'][i]['paragraphs'][j]['qas'])):
                for l in range(0, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers'])):   
                        answer = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']   
                        lemmalist = lemmatizer.lemmatize(answer)
                        data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text'] = lemmalist
    
    print('--LEMMATIZATION FINISHED--') 
    save_file(data, outputfile)

if __name__ == "__main__":
    main()
    
 
                
