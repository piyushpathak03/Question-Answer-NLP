# Create html *outputfile* from JSON *inputfile* with QA data to visualize questions and answers in the text.
from json2html import *
import json
import sys

MAX_PARAGRAPHS = 5
MAX_QUESTIONS = 3
inputfile = 'train_cz_100.json' #sys.argv[1] 
outputfile = 'html.html' #sys.argv[2] 
match_from = 0.99 #sys.argv[3]
match_to = 1.01 #sys.argv[4]
 
#load input json file
def load_file(file):
    with open(file, "r", encoding='utf-8') as read_file:
        data = json.load(read_file) 
    print('--DATA SUCCESSFULLY LOADED--')
    return data

# save data to json file
def save_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
    print('--DATA SUCCESSFULLY SAVED--')    

def main():

    data = load_file(inputfile)
        
    html = """<!DOCTYPE html>
<html>
    <head>
        <style>
            table {
                border: 1px solid black;
                width:100%;
                border-collapse: collapse;
                float: left;
                margin-bottom: 50px;
                background-color:#ccebff;
            }
            td {
                border: 1px solid black;
                widht:80%;
            }
            th {
                border: 1px solid black;
                width:20%;
            }
            h1 {
                text-align: center;               
                background-color:#0099FF;
                color:#ffffff;
                padding: 15px 0px 15px 0px;
            }
            h2 {
                text-align: left;
                font-weight: bold; 
                color: #ffffff;
            }
            body {
                background-color:#80CCFF;
            }
        </style>
    </head>
    <body>
        <h1>Question Answering</h1>"""

    for i in range(0, len(data['data'])):
        topic = data['data'][i]['title']  
        html=html+"""
        <h2>""" + topic + "</h2>"               
        num_paragraphs = min(len(data['data'][i]['paragraphs']), MAX_PARAGRAPHS)
        for j in range(0, num_paragraphs):
            context = data['data'][i]['paragraphs'][j]['context']    
            num_questions = min(len(data['data'][i]['paragraphs'][j]['qas']), MAX_QUESTIONS)
            for k in range(0, num_questions):
                question = data['data'][i]['paragraphs'][j]['qas'][k]['question']                
                num_answers = min(1, len(data['data'][i]['paragraphs'][j]['qas'][k]['answers']))
                for l in range(0, num_answers):                 
                    answer = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['text']  
                    start_idx =  data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_start'] 
                    end_idx = data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_end'] +1# 
                    match =  data['data'][i]['paragraphs'][j]['qas'][k]['answers'][l]['answer_match'] 
                    match = round(match,2)
                    if match>match_from and match<match_to:
                        html=html+"""
        <table>
            <tr>
                <th>CONTEXT</th>
                <td>""" + context[0:start_idx] + "<font color='red'>" + context[start_idx:end_idx] + "</font>" + context[end_idx:len(context)] + """</td>
            </tr>
            <tr>
                <th>QUESTION</th>
                <td>""" + question + """</td>
            </tr>
            <tr>
                <th>ANSWER</th>
                <td>""" + answer + """</td>
            </tr>
        </table>"""
     
    html = html + """
    </body>
</html>"""
    #html=html+""""""
    print('--HTML CREATED CREATED--')
        
    save_file(html, outputfile)
    
if __name__ == "__main__":
    main()
    