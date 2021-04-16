import csv
from flask import Flask,render_template,url_for
from geopy.geocoders import Nominatim
app = Flask(__name__)

"""with open('ville.csv','r') as csv_file:
	"	lat_ville=[]
	long_ville=[]
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:
		geocode = lat_ville.append(row[Lat]), long_ville.append(row[Long])"""
		


@app.route('/')
def map_func():
	#return render_template('leaflet.html')
	return render_template('texte.html')
			
			#'<h1>Bienvenue, veuillez choisir un lieu.</h1>'

@app.route('/Marseille')
def marseille():
	return render_template('Marseille.html')

@app.route('/Brest')
def brest():
	return render_template('Brest.html')

@app.route('/Paris')
def paris():
	return render_template('Paris.html')

@app.route('/France')
def france():
	return render_template('France.html')




if __name__ == '__main__':
    app.run(debug=True)    