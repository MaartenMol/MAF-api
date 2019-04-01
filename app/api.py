#Import required dependencies
from flask import Flask, jsonify, abort, make_response, request
from pymongo import MongoClient
from bson.json_util import dumps
import json
import uuid
import os

#db_ip = os.getenv("db_ip", "Maarten-NB")
#db_port = os.getenv("db_port", "27017")
# Example URI: 'mongodb://host1,host2,host3', replicaSet='rs0'
conUri = os.getenv("conUri", "maarten-nb:27017")
db_name = os.getenv("db_name", "MAF")

#Print some usefull information to console
print("Starting API Server")
print("API Server Version: V1.0")
print("Developed by: Maarten Mol & Rik Merkens (All rights reserved)")
#print("MongoDB Host: " + db_ip)
#print("MongoDB Host: " + db_port)
#print("MongoDB DB Name: " + db_name)

#Setup MongoDB Client
#client = MongoClient(db_ip + ":" + db_port)
client = MongoClient(conUri)
db = client[db_name]

#Define app with Flask
app = Flask(__name__)

#Define error function for JSON error response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

#Define the root
@app.route("/")
def index():
    return "Please use the V1 API! Developed by: Maarten Mol & Rik Merkens (All rights reserved)"

#Define GET USERS
@app.route("/api/v1/users", methods=['GET'])
def get_users():
    try:
        users = db.Users.find()
        return dumps(users), 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define GET WORKOUTS from a USER
@app.route('/api/v1/workouts/email=<email>', methods=['GET'])
def get_workouts(email):
    try:
        if db.Users.count_documents({ "email" : email }, limit = 1) == 1:
            workouts = db.Users.find_one({ "email" : email },{"workouts":1})
            workout = db.Workouts.find({"_id":{"$in":workouts["workouts"]}})
            return dumps(workout), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"getWorkouts" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define GET VIDEOS
@app.route('/api/v1/videos', methods=['GET'])
def get_videos():
    try:
        videos = db.Videos.find()
        return dumps(videos), 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define GET USER
@app.route('/api/v1/users/<field>=<value>', methods=['GET'])
def get_user(field, value):
    try:
        if db.Users.count_documents({ field : value }, limit = 1) == 1:
            user = db.Users.find({ field : value })
            return dumps(user), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"getUser" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define GET WORKOUT
@app.route('/api/v1/workouts/<field>=<value>', methods=['GET'])
def get_workout(field, value):
    try:
        if db.Workouts.count_documents({ field : value }, limit = 1) == 1:
            workout = db.Workouts.find({ field : value })
            return dumps(workout), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"getWorkout" : "workoutNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define GET VIDEO
@app.route('/api/v1/videos/<field>=<value>', methods=['GET'])
def get_video(field, value):
    try:
        if db.Videos.count_documents({ field : value }, limit = 1) == 1:
            video = db.Videos.find({ field : value })
            return dumps(video), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"getVideo" : "videoNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

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
        uid = uuid.uuid4().hex
        if db.Users.count_documents({ 'email': email }, limit = 1) == 0:
            status = db.Users.insert_one({
                "_id" : uid,
                "firstname" : firstname,
                "lastname" : lastname,
                "email" : email,
                "street" : street,
                "city" : city,
                "membership" : membership
            })
            return jsonify({"createUser" : "success"}), 201, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"createUser" : "userEmailDuplicate"}), 403, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define CREATE WORKOUT
@app.route('/api/v1/workouts/user=<email>', methods=['POST'])
def create_workout(email):
    try:
        data = json.loads(request.data)
        workout_type = data['workout_type']
        date = data['date']
        start_time = data['start_time']
        end_time = data['end_time']
        calories = data['calories']
        distance = data['distance']
        comment = data['comment']
        uid = uuid.uuid4().hex
        if db.Users.count_documents({ 'email': email }, limit = 1) == 1:
            status = db.Workouts.insert_one({
                "_id" : uid,
                "workout_type" : workout_type,
                "date" : date,
                "start_time" : start_time,
                "end_time" : end_time,
                "calories" : calories,
                "distance" : distance,
                "comment" : comment
            })
            newValues = { "workouts": uid }
            db.Users.update_one({ "email" : email }, { "$push" : newValues })
            return jsonify({"createWorkout" : "success"}), 201, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"createWorkout" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define CREATE VIDEO
@app.route('/api/v1/videos', methods=['POST'])
def create_video():
    try:
        data = json.loads(request.data)
        title = data['title']
        desc = data['desc']
        length = data['length']
        path = data['path']
        uid = uuid.uuid4().hex
        if db.Videos.count_documents({ 'title': title }, limit = 1) == 0:
            status = db.Videos.insert_one({
                "_id" : uid,
                "title" : title,
                "desc" : desc,
                "length" : length,
                "path" : path
            })
            return jsonify({"createVideo" : "success"}), 201, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"createVideo" : "videoTitleDuplicate"}), 403, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define UPDATE USER
@app.route('/api/v1/users/email=<value>', methods=['PUT'])
def update_user(value):
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
            return jsonify({"updateUser" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"updateUser" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define UPDATE WORKOUT
@app.route('/api/v1/workouts/id=<id>', methods=['PUT'])
def update_workout(id):
    try:
        if db.Workouts.count_documents({ "_id" : id }, limit = 1) == 1:
            data = json.loads(request.data)
            newValues = {}
            if "type" in data:
                type = data['type']
                newValue = { "type": type }
                newValues.update(newValue)
            if "date" in data:
                date = data['date']
                newValue = { "date": date }
                newValues.update(newValue)
            if "start_time" in data:
                start_time = data['start_time']
                newValue = { "start_time": start_time }
                newValues.update(newValue)
            if "end_time" in data:
                end_time = data['end_time']
                newValue = { "end_time": end_time }
                newValues.update(newValue)
            if "calories" in data:
                calories = data['calories']
                newValue = { "calories": calories }
                newValues.update(newValue)
            if "distance" in data:
                distance = data['distance']
                newValue = { "distance": distance }
                newValues.update(newValue)
            if "comment" in data:
                comment = data['comment']
                newValue = { "comment": comment }
                newValues.update(newValue)        
            db.Workouts.update_one({ "_id" : id }, { "$set" : newValues })
            return jsonify({"updateWorkout" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"updateWorkout" : "workoutNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define UPDATE VIDEO
@app.route('/api/v1/videos/id=<value>', methods=['PUT'])
def update_video(value):
    try:
        if db.Videos.count_documents({ "_id" : value }, limit = 1) == 1:
            data = json.loads(request.data)
            newValues = {}
            if "title" in data:
                title = data['title']
                newValue = { "title": title }
                newValues.update(newValue)
            if "desc" in data:
                desc = data['desc']
                newValue = { "desc": desc }
                newValues.update(newValue)
            if "length" in data:
                length = data['length']
                newValue = { "length": length }
                newValues.update(newValue)
            if "path" in data:
                path = data['path']
                newValue = { "path": path }
                newValues.update(newValue)
            db.Videos.update_one({ "_id" : value }, { "$set" : newValues })
            return jsonify({"updateVideo" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"updateVideo" : "videoNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define DELETE USER with EMAIL
@app.route('/api/v1/users/email=<value>', methods=['DELETE'])
def delete_user(value):
    try:
        if db.Users.count_documents({ "email" : value }, limit = 1) == 1:
            workouts = db.Users.find_one({ "email" : value },{"workouts":1})
            db.Workouts.delete_many({"_id":{"$in":workouts["workouts"]}})
            db.Users.delete_one({ "email" : value })
            return jsonify({"deleteUser" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"deleteUser" : "userNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define DELETE WORKOUT with ID
@app.route('/api/v1/workouts/user=<email>/id=<value>', methods=['DELETE'])
def delete_workout(email, value):
    try:
        if db.Workouts.count_documents({ "_id" : value }, limit = 1) == 1:
            db.Workouts.delete_one({ "_id" : value })
            newValues = { "workouts": value }
            db.Users.update_one({ "email" : email }, { "$pull" : newValues })
            return jsonify({"deleteWorkout" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"deleteWorkout" : "workoutNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define DELETE VIDEO with ID
@app.route('/api/v1/videos/id=<value>', methods=['DELETE'])
def delete_video(value):
    try:
        if db.Videos.count_documents({ "_id" : value }, limit = 1) == 1:
            db.Videos.delete_one({ "_id" : value })
            return jsonify({"deleteVideo" : "success"}), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return jsonify({"deleteVideo" : "videoNotFound"}), 404, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return dumps({'error' : str(e)}), 500, {'Content-Type': 'application/json; charset=utf-8'}

#Define main APP
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)