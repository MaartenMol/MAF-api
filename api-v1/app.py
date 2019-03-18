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

#Define UPDATE USER
@app.route('/api/v1/users/<int:test_id>', methods=['PUT'])
def update_test(test_id):
    test = [test for test in tests if test['id'] == test_id]
    if len(test) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    test[0]['title'] = request.json.get('title', test[0]['title'])
    test[0]['description'] = request.json.get('description', test[0]['description'])
    test[0]['done'] = request.json.get('done', test[0]['done'])
    return jsonify({'task': test[0]})

#Define DLETE USER
@app.route('/api/v1/users/<int:test_id>', methods=['DELETE'])
def delete_task(test_id):
    test = [test for test in tests if test['id'] == test_id]
    if len(test) == 0:
        abort(404)
    test.remove(test[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)