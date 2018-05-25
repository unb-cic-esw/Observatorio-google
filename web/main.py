import boto3
from flask import Flask, jsonify
import json
import os

s3 = boto3.resource('s3')
bucket = s3.Bucket(os.environ['S3_BUCKET'])

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
	fileName = './resultados/' + date + '/pup_' + actor + '/pup_' + actor + '.json'
	data = ""
	for obj in bucket.objects.all():
		if(obj.key == fileName):
			data = obj.get()['Body'].read().decode('utf8')
	return jsonify(json.loads(data))

@app.route('/dates', methods = ['GET'])
def list_dates():
	fileName = 'all_dates.json'
	data = ""
	for obj in bucket.objects.all():
		if(obj.key == fileName):
			data = obj.get()['Body'].read().decode('utf8')
	return jsonify(json.loads(data))

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
