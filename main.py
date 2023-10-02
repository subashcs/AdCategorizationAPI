from flask import Flask, jsonify, request, json
import pickle
import pandas as pd
import numpy as np
import nltk
import re


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(nltk.corpus.stopwords.words('english'))

#prepare text clean function

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
   ## we dont need text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS) # delete stopwors from text
    return text
    

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@app.route('/')
def hello_world():
    return None

@app.route('/<content>')
def show_user_profile(content):
    ToPredict=clean_text(content)
    result = loaded_model.predict([ToPredict])
    res = ''.join(str(e) for e in result)
    return jsonify({"category":res})

@app.route('/test')
def testData():
    return jsonify({"result":"success"})   

@app.route('/classify',methods = ['POST'])
def classify():
    data = request.get_json()
    content = data['content']
    str1 = ''.join(str(e) for e in content)
    ToPredict=clean_text(content)
    result = loaded_model.predict([ToPredict])
    res = ''.join(str(e) for e in result)
    return jsonify({"category":res})

 