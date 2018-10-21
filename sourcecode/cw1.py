from flask import Flask, render_template, jsonify, abort, json, url_for, request, redirect
app = Flask(__name__)

with open('static/data/swords.json') as swords_json:
	swords = json.load(swords_json)

@app.route('/')
def root():
	return redirect(url_for('home'))
	
@app.route('/home/')
def home():
	return render_template('home.html'), 200

@app.route('/swords/', methods=['GET'])
def swords_list():
	return render_template('swords.html', swords=swords)

@app.route('/swords/<sword_name>/')
def sword_details(sword_name):
	sword_names=[]

	for sword in swords:
		sword_names.append(sword["name"])
	
	if sword_name in sword_names:
		return render_template('sword_details.html', swords=swords, sword_name=sword_name)
		
	else:
		abort(404)

material_names=[]

for sword in swords:
	material_names.append(sword["material"])

material_names_distinct= sorted(list(set(material_names)))

@app.route('/materials/')
def materials():		
	return render_template('materials.html', swords=swords, material_names_distinct=material_names_distinct)

@app.route('/materials/<material_name>/')
def material_weapons(material_name):
	if material_name in material_names_distinct:
		return render_template('material_weapons.html', swords=swords, material_names_distinct=material_names_distinct, material_name=material_name)
	else:
		abort(404)

@app.route('/upload/', methods=['POST','GET'])
def upload():
	if request.method == 'POST':
		print request.form
		name = request.form['name']
		material = request.form['material']
		owner = request.form['owner']
		status = request.form['status']
		image = request.files['datafile']

		image.save('static/images/'+ name + '.png')

		sword = {
			"name" : name,
			"material" : material,
			"owner" : owner,
			"status" : status
			}
		
		swords.append(sword)
		
		with open('static/data/swords.json', 'a') as swords_json:
			json.dump(sword, swords_json)
		
		return redirect(url_for('swords'))

	else:
		return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(error):
	return "This page does not exist ya dingus", 404

if __name__ == ("__main__"):
	app.run(host='0.0.0.0', debug=True)
