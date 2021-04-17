from flask import Flask, render_template, request
import joblib
import numpy
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV

import numpy as np

import spacy
import re
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")

bad_words = np.load("trained_model/bad_words.npy", allow_pickle=True).tolist()
bad_words_patterns = [nlp(text) for text in bad_words]
matcher = PhraseMatcher(nlp.vocab)
matcher.add('BAD_WORDS', None, *bad_words_patterns)

model = joblib.load("trained_model/model-V2.joblib")
vectorizer = joblib.load("trained_model/vectorizer-V2.joblib")
label = ["Non Abusive", "Abusive"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    user_input = request.args.get('jsdata')
    X = vectorizer.transform([user_input])
    y = model.predict(X)
    proba = model.predict_proba(X)
    y_label = label[y[0]]
    y_probability = np.max(proba)*100
    final_res = str(y_label)+":"+ str(y_probability)
    print(final_res)
    return render_template('prediction.html', prediction=final_res)

@app.route("/censor", methods=["POST", "GET"])
def censor():
    data = request.args.get("data")
    data = data.lower()
    doc = nlp(data)
    matches = matcher(doc)
    text = data
    for match_id, start, end in matches:
        span = doc[start: end]
        len_of_word = len(span.text)
        censor_ = "*" * len_of_word
        text = re.sub(span.text, censor_, text)
    return render_template('censor.html', censor_=text)

@app.route('/Privacy-Policy', methods=['GET', 'POST'])
def pp():
    return render_template('Privacy Policy.html')

if __name__ == '__main__':
    app.run(debug=True)
