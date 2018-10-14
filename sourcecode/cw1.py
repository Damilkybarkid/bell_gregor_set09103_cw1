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
		},

		{
		'name': 'Hearteater',
		'material': 'Castle-forged Steel',
		'owner': 'Joffrey Baratheon',
		'status': 'Unknown'
		},

		{
		'name': 'Heartsbane',
		'material': 'Valyrian Steel',
		'owner': 'House Tarly',
		'status': 'With Samwell Tarly'
		},

		{
		'name': 'Ice',
		'material': 'Valyrian Steel',
		'owner': 'House Stark (formerly)',
		'status': 'Melted down and reforged into Oathkeeper and Widow\'s Wail'
		},

		{
		'name': 'Lady Forlorn',
		'material': 'Valyrian Steel',
		'owner': 'House Corbray',
		'status': 'With the head of House Corbray'
		},

		{
		'name': 'Lightbringer',
		'material': 'Unknown',
		'owner': 'Uncertain (Formerly Stannis Baratheon, allegedly Azor Ahai)',
		'status': 'Uncertain, last seen with Stannis Baratheon at the Battle of Winterfell'
		},

		{
		'name': 'Lion\'s Tooth',
		'material': 'Castle-forged Steel',
		'owner': 'Joffrey Baratheon',
		'status': 'Lost in the waters of the Trident'
		},

		{
		'name': 'Longclaw',
		'material': 'Valyrian Steel',
		'owner': 'Jon Snow',
		'status': 'With Jon Snow'
		},

		{
		'name': 'Needle',
		'material': 'Castle-forged Steel',
		'owner': 'Arya Stark',
		'status': 'With Arya Stark'
		},

		{
		'name': 'Oathkeeper',
		'material': 'Valyrian Steel',
		'owner': 'Brienne of Tarth',
		'status': 'With Brienne of Tarth'
		},

		{
		'name': 'Two Brothers',
		'material': 'Wood',
		'owner': 'Ryon Forrester, Rodrik Forrester',
		'status': 'At Ironrath'
		},

		{
		'name': 'Valyrian Steel Dagger',
		'material': 'Valyrian Steel',
		'owner': 'Arya Stark',
		'status': 'With Arya Stark'
		},

		{
		'name': 'Widow\'s Wail',
		'material': 'Valyrian Steel',
		'owner': 'Ser Jaime Lannister',
		'status': 'With Ser Jaime Lannister'
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
