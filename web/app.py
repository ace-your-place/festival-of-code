from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cakes')
def cakes():
	return 'cakes are awesome'

@app.route('/<location_input>')
def map():
	return render_template('map.html', location=location_input)

if __name__ == '__main__':
	app.run(debug=True)
