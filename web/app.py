from flask import Flask, render_template, request
from getLocation import getLocation, getLocationRand

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
	if request.method == 'POST':
		lat_longs = getLocation(crime = request.form['crime'], education = request.form['education'])[0]
		return render_template('map.html', locations = lat_longs)

@app.route('/map', methods=['GET'])
def map():
	l = request.args.get('location')
	return render_template('map.html', location = l)

if __name__ == '__main__':
	app.run(debug=True)
