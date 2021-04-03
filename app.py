from flask import Flask, render_template, request
import joblib
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.calibration import CalibratedClassifierCV
from sklearn.svm import LinearSVC
import numpy as np

model = joblib.load("trained_model/bestmodel.joblib")
vectorizer = joblib.load("trained_model/vectorizer.joblib")
label = ["Neutral", "Abusive"]
app = Flask(__name__)

res = ""
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
    return render_template('prediction.html', prediction = final_res)



if __name__ == '__main__':
    app.run(debug=True)