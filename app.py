from stepper_mover_test import move_stepper
from flask import jsonify, request, Flask
from waitress import serve
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": ""}})
cors1 = CORS(app, resources={r"/move-motor": {"origins": ""}})
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def first():
    return ('<h1>Flask Api Root</h1>\n'
            '<p>A prototype API for microservice integration.</p>\n'
            '<p> Your testing endpoint should be like: \'/index?email=sarthak1@gmail.com&courseid=570014&eventid=0&chapterid=11856279&version=16-07-2020 12:48:51\'</p>\n'
            '<p>version is optional</p>\n')


@app.route('/move-motor', methods=['GET'])
def index():
    try:
        if 'direction' in request.args:
            direction = request.args['direction']
            move_stepper(direction)
            return jsonify('moved')
            # return jsonify(email, courseid, chapterid, eventid, version)
    except Exception as e:
        return jsonify('some issue found. have a look on it')

    return jsonify('all arguments needed')


if __name__ == '_main_':
    app.run(host='0.0.0.0')
