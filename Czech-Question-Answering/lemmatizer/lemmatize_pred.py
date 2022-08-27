# Lemmatize *inputfile* with predicted answers using MorphoDita and save the results to the *outputfile*.
# Lemmatize model can be extracted from http://hdl.handle.net/11234/1-1836
import json
import sys
import requests
import xml.etree.ElementTree as ET
import time 
import lemmatizer

inputfile = 'predictions_czu84.json'
outputfile = 'predictions_czu84_lemmatized.json'

# load input json file
def load_file(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file) 
    print('--DATA SUCCESSFULLY LOADED--', file=sys.stderr)
    return data

# save data to json file
def save_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f,ensure_ascii=False)
    print('--DATA SUCCESSFULLY SAVED--', file=sys.stderr)    

def main():
    data = load_file(inputfile)

    for (k, v) in data.items():
        lemmalist = lemmatizer.lemmatize(v)
        data[k] = lemmalist

    print('--LEMMATIZATION FINISHED--', file=sys.stderr) 
    save_file(data, outputfile)

if __name__ == "__main__":
    main()
    

 
                
