from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	print("received the values")
	return render_template('index.html')

@app.route('/show', methods = ['GET' ,'POST'])
def show():
	t = request.form['txt']
	'''
	age = request.form['age']
	db = request.form ['dateofbirth']
	print("asdfadfasdfasdffd")
	'''
	return render_template('pass.html', txt = t)

if __name__ == '__main__':
	app.run(debug=True)
