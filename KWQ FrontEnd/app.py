from flask import Flask, render_template, request
import nltk
nltk.download('all')
from np_extractor import get_nps_from_text, get_nps_from_tokens
from nltk import tokenize
import random

app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/show', methods = ['GET' ,'POST'])
def show():
	t = request.form['txt']
	arr = tokenize.sent_tokenize(t)
	
	kw = []
	booga = ""
	for sentence in arr:
		keywords = get_nps_from_text(sentence)
		kw.append(keywords)
		for words in keywords:
			sentence = sentence.replace(words, '___')
		booga = booga +  sentence + " "

	k = []
	for i in kw:
		for j in i:
			k.append(j)

	random.shuffle(k)

	kwStr = ""
	for i in k:
		kwStr = kwStr +  i + ", "    
	'''
	age = request.form['age']
	db = request.form ['dateofbirth']
	print("asdfadfasdfasdffd")
	'''
	return render_template('pass.html', txt = booga, wordbank = kwStr)

if __name__ == '__main__':
	app.run(debug=True)
