# translate answers of outpuf file from model using lindat translator 
import sys
import requests
import json

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
    del(data['scores'])
    for (k, v) in data.items():
        data[k] = translate(str(v))
    print('--TRANSLATION FINISHED--') 
    save_file(data, outputfile)

if __name__ == "__main__":
    main()
    
 
                
