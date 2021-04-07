# Abusive-Language-Detection
![Made with python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white")
![Flask](https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white)
![Made with HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Uses CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

[![deployed](https://heroku-badges.herokuapp.com/?app=abusive-language-detect)](https://abusive-language-detect.herokuapp.com/)

## Web App
Web App is accessible through this link: [Abusive Language Detection](https://abusive-language-detect.herokuapp.com/)

## Description
<p align="center">
  <img width="460" height="300" src="https://github.com/Sumit189/Abusive-Language-Detection/blob/main/images_for_readme/wordcloud.png">
</p>

This project is made for the detection of the Abusive Language from text provided by users. The  model is trained with latest Sklearn Version 0.24.1 on the [Abusive/Non Abusive dataset.](https://github.com/vzhou842/profanity-check/blob/master/profanity_check/data/clean_data.csv)
### Classifiers
For this project we trained 3 models: 
  1. Random Forest
  2. Calibrated Classifier
  3. Decision Tree

<p align="center">
  <img width="460" height="300" src="https://github.com/Sumit189/Abusive-Language-Detection/blob/main/images_for_readme/Accuracy.PNG">
</p>
Calibrated Classifier performed well as compared to other two classifiers. For final model, Calibrated Classifier was trained.

### Censor Abusive Words
To censor abusive words we have used the Spacy PhraseMatcher which matches words of user input to the [bad_words.txt](https://github.com/Sumit189/Abusive-Language-Detection/blob/main/notebook/data/bad_words.text) and replace the matched words with asterisk(*).

## Flask App
For deployment of the website we have created an HTML website with <img alt="Flask" src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/>. The model works in real time, which means for every typed letter it will make prediction for the sentiment of the whole sentence. 

### Abusive Demo
![Abusive](https://github.com/Sumit189/Abusive-Language-Detection/blob/main/images_for_readme/Abusive.PNG)

### Censored Demo
![Censored](https://github.com/Sumit189/Abusive-Language-Detection/blob/main/images_for_readme/Censored.PNG)
