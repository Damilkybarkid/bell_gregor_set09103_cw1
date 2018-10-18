from flask import Flask, render_template, jsonify, abort, json, url_for, request
app = Flask(__name__)

with open('static/data/swords.json') as swords_json:
	swords = json.load(swords_json)

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

@app.route('/upload/', methods=['POST','GET'])
def upload():
	if request.method == 'POST':
		print request.form
		name = request.form['name']
		material = request.form['material']
		owner = request.form['owner']
		status = request.form['status']

		sword = {
			"name" : name,
			"material" : material,
			"owner" : owner,
			"status" : status
			}
		
		swords.append(sword)
		
		with open('static/data/swords.json', 'a') as swords_json:
			json.dump(sword, swords_json)
		
		return jsonify(swords)

	else:
		page ='''
			<html>
				<body>
					<form action ="" method="post" name="form">
						<label for="name">Name:</label>
						<input type="text" name="name" id="name"/>
						<label for="material">Material:</label>
						<input type="text" name="material" id="material"/>
						<label for="owner">Owner:</label>
						<input type="text" name="owner" id="owner"/>
						<label for="status">Status:/>
						<input type="text" name="status" id="status"/>
						<input type="submit" name="submit" id="submit"/>
					</form>
				</body>
			</html>
		'''

	return page

if __name__ == ("__main__"):
	app.run(host='0.0.0.0', debug=True)
