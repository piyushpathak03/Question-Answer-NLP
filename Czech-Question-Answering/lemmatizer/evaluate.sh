#!/bin/bash
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc81.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc83.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc84.json

python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc11.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc13.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czc14.json

python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu81.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu83.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu84.json

python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu11.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu13.json
python evaluate-v1.1.py dev-100-lemmatized.json predictions_czu14.json