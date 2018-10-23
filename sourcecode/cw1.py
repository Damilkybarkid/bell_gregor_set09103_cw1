# The main python file containing all flask routing and methods

# Import relevant libraries
from flask import Flask, render_template, abort, json, url_for, request, redirect
app = Flask(__name__)

# Load in the JSON file
with open('static/data/swords.json') as swords_json:
	swords = json.load(swords_json)

# The default page, redirects to /home/
@app.route('/')
def root():
	return redirect(url_for('home'))

# Display the home.html template	
@app.route('/home/')
def home():
	return render_template('home.html'), 200

# Displat the swords.html template
@app.route('/swords/', methods=['GET'])
def swords_list():
	return render_template('swords.html', swords=swords)

# Loop through a;; the swords in the JSON file and if sword_name does not exist in the list, give a 404 error
# If it does exist, display the sword_details.html template
@app.route('/swords/<sword_name>/')
def sword_details(sword_name):
	sword_names=[]

	for sword in swords:
		sword_names.append(sword["name"])
	
	if sword_name in sword_names:
		return render_template('sword_details.html', swords=swords, sword_name=sword_name)
		
	else:
		abort(404)

# Loop through all swords in the JSON file and add all the owner names to a list
# Then display the owners.html template
@app.route('/owners/')
def owners():
	owner_names=[]

	for sword in swords:
		owner_names.append(sword["owner"])

	owner_names_distinct= sorted(list(set(owner_names))) # This line removes duplicates from the list and sorts the list alphabetically. 
	
	return render_template('owners.html', swords=swords, owner_names_distinct=owner_names_distinct)


# Loop through a;; the swords in the JSON file and if owner_name does not exist in the list, give a 404 error
# If it does exist, display the owner_weapons.html template
@app.route('/owners/<owner_name>/')
def owner_weapons(owner_name):
	owner_names=[]

	for sword in swords:
		owner_names.append(sword["owner"])
	
	owner_names_distinct = sorted(list(set(owner_names))) # This line removes duplicates from the list and sorts the list alphabetically

	if owner_name in owner_names_distinct:
		return render_template('owner_weapons.html', swords=swords, owner_names_distinct=owner_names_distinct, owner_name=owner_name)

	else:
		abort(404)


# Loop through all swords in the JSON file and add all the material names to a list
# Then display the materials.html template
@app.route('/materials/')
def materials():		
	material_names=[]
	
	for sword in swords:
		material_names.append(sword["material"])
	
	material_names_distinct= sorted(list(set(material_names))) # This line removes duplicates from the list and sorts the list alphabetically.
	
	return render_template('materials.html', swords=swords, material_names_distinct=material_names_distinct)

# Loop through a;; the swords in the JSON file and if material_name does not exist in the list, give a 404 error
# If it does exist, display the material_weapons.html template
@app.route('/materials/<material_name>/')
def material_weapons(material_name):
	material_names=[]
	
	for sword in swords:
		material_names.append(sword["material"])
	
	material_names_distinct= sorted(list(set(material_names)))

	if material_name in material_names_distinct:
		return render_template('material_weapons.html', swords=swords, material_names_distinct=material_names_distinct, material_name=material_name)
	
	else:
		abort(404)

# If the request method is not POST, serve the user with the upload form stored in upload.html
# If it is POST, save the data from the form into the JSON file and redirect the user to /swords/
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
		
		with open('static/data/swords.json', 'w') as swords_json:
			json.dump(swords, swords_json)
		
		return redirect(url_for('swords_list'))

	else:
		return render_template('upload.html')

# If the request method is not POST, serve the user with the delete form stored in delete.html
# If it is POST, remove the sword listed in the form from the JSON file and redirect the user to /swords/
@app.route('/delete/', methods=['POST','GET'])
def delete():
	if request.method == 'POST':
		print request.form
		name = request.form['name']
		
		for sword in swords:
			if name == sword["name"]:
				swords.remove(sword)
		
		with open('static/data/swords.json', 'w') as swords_json:
			json.dump(swords, swords_json)

		return redirect(url_for('swords_list'))

	else:
		return render_template('delete.html')

# Check if sword_name exists in the JSON file and if it does, remove it
# Then redirect the user to /swords/
@app.route('/delete/<sword_name>/', methods=['GET'])
def delete_weapon(sword_name):
	for sword in swords:
		if sword_name == sword["name"]:
			swords.remove(sword)
	with open('static/data/swords.json', 'w') as swords_json:
		json.dump(swords, swords_json)

	return redirect(url_for('swords_list'))

# Dislay the 404.html template if a 404 error is generated
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == ("__main__"):
	app.run(host='0.0.0.0', debug=True)
