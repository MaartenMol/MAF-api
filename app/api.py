#Import required dependencies
from flask import Flask, jsonify, abort, make_response, request
from pymongo import MongoClient
from bson.json_util import dumps
import json

#Setup MongoDB Client
client = MongoClient('Maarten-NB:27017')
db = client.MAF

#Define app with Flask
app = Flask(__name__)



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
def get_users():
    try:
        users = db.Users.find()
        return dumps(users), 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)})



#Define GET USER
@app.route('/api/v1/users/<field>/<value>', methods=['GET'])
def get_test(field, value):
    try:
        user = db.Users.find({ field : value })
        return dumps(user), 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 404, {'Content-Type': 'application/json; charset=utf-8'}



#Define CREATE USER
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    try:
        data = json.loads(request.data)
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        street = data['street']
        city = data['city']
        membership = data['membership']
        if db.Users.count_documents({ 'email': email }, limit = 1) == 0:
            status = db.Users.insert_one({
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "street" : street,
                "city" : city,
                "membership" : membership
            })
            return dumps({'message' : 'SUCCESS'})
        else:
            abort(400)
    except Exception as e:
        return dumps({'error' : str(e)})



#Define UPDATE USER
@app.route('/api/v1/users/email/<value>', methods=['PUT'])
def update_test(value):
    try:
        if db.Users.count_documents({ "email" : value }, limit = 1) == 1:
            data = json.loads(request.data)

            newValues = {}

            if "firstname" in data:
                firstname = data['firstname']
                newValue = { "firstname": firstname }
                newValues.update(newValue)

            if "lastname" in data:
                lastname = data['lastname']
                newValue = { "lastname": lastname }
                newValues.update(newValue)

            if "email" in data:
                email = data['email']
                newValue = { "email": email }
                newValues.update(newValue)

            if "street" in data:
                street = data['street']
                newValue = { "street": street }
                newValues.update(newValue)

            if "city" in data:
                city = data['city']
                newValue = { "city": city }
                newValues.update(newValue)

            if "membership" in data:
                membership = data['membership']
                newValue = { "membership": membership }
                newValues.update(newValue)           

            db.Users.update_one({ "email" : value }, { "$set" : newValues })
            
            return jsonify({"update" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
            
        else:
            return jsonify({"update" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
            
    except Exception as e:
        return dumps({'error' : str(e)}), 404, {'Content-Type': 'application/json; charset=utf-8'}



#Define DELETE USER with EMAIL
@app.route('/api/v1/users/email/<value>', methods=['DELETE'])
def delete_task(value):
    try:
        if db.Users.count_documents({ "email" : value }, limit = 1) == 1:
            db.Users.delete_one({ "email" : value })
            return jsonify({"delete" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"delete" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
            
    except Exception as e:
        return dumps({'error' : str(e)}), 404, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)