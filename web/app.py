from flask import Flask, render_template, request
from getLocation import getLocation

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['GET'])
def form():
	crime_data = 0#equest.form.crime
	education_data = 1#request.form.education
	lat_long = getLocation(crime=crime_data,education=education_data)
	return render_template('map', latitude = lat_long[0], longitude = lat_long[1])

@app.route('/map', methods=['GET'])
def map():
	l = request.args.get('location')
	return render_template('map.html', location = l)

if __name__ == '__main__':
	app.run(debug=True)