#Import required dependencies
from flask import Flask, jsonify, abort, make_response, request

#Define app with Flask
app = Flask(__name__)

#Define test data
tests = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

#Define error function for JSON error response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Define the root
@app.route('/')
def index():
    return "Please use the V1 API!"

#Define GET USERS
@app.route('/api/v1/users', methods=['GET'])
def get_tests():
    return jsonify({'tests': tests})

#Define GET USER [ID]
@app.route('/api/v1/users/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = [test for test in tests if test['id'] == test_id]
    if len(test) == 0:
        abort(404)
    return jsonify({'test': test[0]})

#Define CREATE USER
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'title' in request.json:
        abort(400)
    test = {
        'id': tests[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tests.append(test)
    return jsonify({'test': test}), 201

if __name__ == '__main__':
    app.run(debug=True)