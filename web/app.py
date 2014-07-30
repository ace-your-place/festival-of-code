from flask import Flask, render_template, request
app = Flask(__name__)
loc = []
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'cakes are awesome'

@app.route('/map', methods=['GET'])
def map():
	lat = request.args.get('latitude')
	lng = request.args.get('longitude')
	l = request.args.get('location')
	return render_template('map.html', latitude = lat, longitude = lng, location = l)

if __name__ == '__main__':
	app.run(debug=True)
