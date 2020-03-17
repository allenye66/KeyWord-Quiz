from flask import Flask, render_template, request
from nltk import tokenize
from np_extractor import get_nps_from_text, get_nps_from_tokens


app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/show', methods = ['GET' ,'POST'])
def show():
	t = request.form['txt']
	arr = tokenize.sent_tokenize(t)
	booga = ""
	for sentence in arr:
		keywords = get_nps_from_text(sentence)
		for words in keywords:
			sentence = sentence.replace(words, '___')
		booga = booga + sentence

	'''
	age = request.form['age']
	db = request.form ['dateofbirth']
	print("asdfadfasdfasdffd")
	'''
	return render_template('pass.html', txt = booga)

if __name__ == '__main__':
	app.run(debug=True)
