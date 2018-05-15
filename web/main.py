from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
	return "Observatorio Google" 

@app.route('/actors', methods = ['GET'])
def actors():
	with open('actors/actors.json') as data:
		return jsonify(json.load(data))

@app.route('/<date>/<actor>/all', methods = ['GET'])
def list_links(date, actor):
	fileName = 'resultados/' + date + '/pup_' + actor + '/pup_' + actor + '.json'
	with open(fileName) as data:
		return jsonify(json.load(data))

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
