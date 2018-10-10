from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route('/swords/')
def swords():
	return render_template('swords.html')

@app.route('/daggers/')
def daggers():
	return render_template('daggers.html')

if __name__ == ("__main__"):
	app.run(host='0.0.0.0', debug=True)
