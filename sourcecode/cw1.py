from flask import Flask, render_template, jsonify, abort, json, url_for
app = Flask(__name__)

swords = [
		{
		'name':'Blackfyre',
		'material': 'Valyrian Steel',
		'owner': 'House Targaryen',
		'status': 'Missing'
		},

		{
		'name': 'Brightroar',
		'material': 'Valyrian Steel',
		'owner': 'Tommen II Lannister',
		'status': 'Missing'
		},

		{
		'name': 'Dark Sister',
		'material': 'Valyrian Steel',
		'owner': 'Visenya Targaryen, Daemon Targaryen, Aemon Targaryen, Brynden Rivers',
		'status': 'Missing'
		},

		{
		'name': 'Dawn',
		'material': '"Fallen Star" Metal',
		'owner': '"The Sword of the Morning" (House Dayne)',
		'status': 'Returned to Starfall by Eddard Stark'
		},
		
		{
		'name': 'Forrester Greatsword',
		'material': 'Unknown',
		'owner': 'House Forrester',
		'status': 'Unknown (likely in the posession of House Whitehill)'		
		}
	]

@app.route('/')
def root():
	return render_template('home.html'), 200

@app.route('/daggers/')
def daggers():
	return render_template('daggers.html')

@app.route('/swords/', methods=['GET'])
def swords_list():
	return render_template('swords.html', swords=swords)

@app.route('/swords/<sword_name>/')
def sword_details(sword_name):
	return render_template('sword_details.html', swords=swords, sword_name=sword_name)

if __name__ == ("__main__"):
	app.run(host='0.0.0.0', debug=True)
