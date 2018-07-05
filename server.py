"""
Server to send data from Python backend to React frontend
Sending JSON to frontend: https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
Reading JSON from frontend: https://stackoverflow.com/questions/30673079/send-json-to-flask-using-requests
"""
from datetime import timedelta  
from flask import Flask, request, jsonify, make_response, current_app
from functools import update_wrapper
app = Flask(__name__)

def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
@crossdomain(origin='*')
def test():
	args = request.args
	output = {}
	output['Model'] = args['model']
	output['Release_date'] = args['releaseDate']
	output['Zoom'] = args['zoom']
	output['price'] = 10
	return jsonify(output)

if __name__ == '__main__':
   app.run()