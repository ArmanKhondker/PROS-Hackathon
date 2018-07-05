"""
Server to send data from Python backend to React frontend
Sending JSON to frontend: https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
Reading JSON from frontend: https://stackoverflow.com/questions/30673079/send-json-to-flask-using-requests
"""

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def test():
	args = request.args
	output = {}
	output['Model'] = args['model']
	output['Release_date'] = args['release_date']
	output['Zoom'] = args['zoom']
	return jsonify(output)

if __name__ == '__main__':
   app.run()