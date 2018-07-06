"""
Server to send data from Python backend to React frontend
"""
from datetime import timedelta  
from flask import Flask, request, jsonify, make_response, current_app
from functools import update_wrapper
from predict import boost_predict
from loop import loop
import pickle

app = Flask(__name__)
videos = {'Canon': ['q1ERQ92k3mk', 'e7zDuWjC4gQ', 'XX6eO8ivkq0', 'r4pZQepv4r4', 'AXuM7mw9gyg', 'wOIuZ1kqOcE', 'W71YkswXg3I', 'K_z3dIKqSuQ', 'btaesOmA_ro', 'FflMjrzBS9E'],
            'Nikon': ['06B0BeAo2E0', 'Z3a9RHaDFF0', 'cugK3f6Q6cQ', 'xH5s1nmbBfc', 'io3MWcwXjJg', '0uPSmGxhNWQ', 'A_OMIRHXynQ', 'p36JKnSOBLY', '8NIi5b791GU', 'utKjjzTaQoQ'],
            'Sony': ['jDcB36B7HDM', 'oqtxVSlxM90', 'AxRbtI5EeF0', 'NROsTlGeqB8', 'cx20nTPZjes', 'aCEkhwAM7T8', 'ry0uTWJf970', 'M7qnb69nVgw', 'wUJc83wV6iA', '8P5irosYUnA'],
            'Panasonic': ['wbLpH5TewnM', '6SQdPxFqUp4', 'cJKRgMPk1BU', 'xEpuGf9hD4w', 'juBkGij2rEs', 'G4485EViAVA', 'Xv2OWv6pWVM', 'yGgJlToYVFc', 'Hs3dkdtKimQ', 'NXdIHAgOB7A'],
            'Olympus': ['eWsSSFQCP4o', 'BP3tznYjMlg', 'VwnCAz3WtRg', '1FVD5kM9F2w', 'ioKpVCsEfhE', 'SpYrIqz09kU', 'E72u0hHWhlU', '0uQKYgQaNHQ', 'WMg5BZbyMo4', 'IfLL9qmY2Ic']}

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
def boost():
	args = request.args
	model = pickle.load(open('prediction_model.sav', 'rb'))
	out = {}
	out['price'] = boost_predict(model,args['model'],args['releaseDate'],args['maxRes'],args['lowRes'],args['effPix'],args['zoomW'],args['zoomT'],args['normalFocus'],args['macroFocus'],args['storage'],args['weight'],args['dimension'])[0]
	out['sentimentScore'] = loop(videos[args['model']])
	return jsonify(out)

if __name__ == '__main__':
   app.run()