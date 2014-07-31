from flask import Flask, render_template, request
from getLocation import getLocation

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form', methods=['POST','GET'])
def form():
	if request.method == 'POST':
#		print request.form['crime']
#		print request.form['education']
#		crime_data = request.form['crime']
#		education_data = request.form('education')
		lat_long = getLocation(crime = request.form['crime'], education = request.form['education'])
		return render_template('map.html', location = lat_long)

@app.route('/map', methods=['GET'])
def map():
	l = request.args.get('location')
	return render_template('map.html', location = l)

if __name__ == '__main__':
	app.run(debug=True)