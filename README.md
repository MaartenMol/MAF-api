# MAF-api
## Docker Deploy
```docker run --name maf-db -p 27017:27017 -d mongo```

```docker run --name maf-api -d -e db_ip="maf-db" -p 5000:5000 mennoaltijdfit/api```
### Environment Flags
| Flag | Description |
| ------------- | ------------- |
| db_ip | IP or Hostname of the MongoDB server |
| db_port | Port of the MongoDB server |
| db_name | Name of the Database to use |


## API Design
### User API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/users/ | Retrieve list of users |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/users/[searchField]=[searchTerm] | Retrieve a user |
| :heavy_check_mark: | POST | http://[hostname]/api/v1/users/ | Create a user |
| :heavy_check_mark: | PUT | http://[hostname]/api/v1/users/email=[email] | Update a User |
| :heavy_check_mark: | DELETE | http://[hostname]/api/v1/users/email=[email] | Delete a user |

### Workout API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/workouts/email=[email] | Retrieve a list of workouts from a user |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/workouts/[searchField]=[searchTerm] | Retrieve a workout |
| :heavy_check_mark: | POST | http://[hostname]/api/v1/workouts/user=[id] | Create a workout for user |
| :heavy_check_mark: | PUT | http://[hostname]/api/v1/workouts/id=[id] | Update a Workout |
| :heavy_check_mark: | DELETE | http://[hostname]/api/v1/workouts/id=[id] | Delete a workout |

### Video API
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/videos/ | Retrieve list of videos |
| :heavy_check_mark: | GET | http://[hostname]/api/v1/videos/[searchField]=[searchTerm] | Retrieve a video |
| :heavy_check_mark: | POST | http://[hostname]/api/v1/videos/ | Create a video |
| :heavy_check_mark: | PUT | http://[hostname]/api/v1/videos/id=[id] | Update a Video |
| :heavy_check_mark: | DELETE | http://[hostname]/api/v1/videos=[id] | Delete a video |

### Fields
#### Users
* **_id**: Unique number per user
* **firstname**: Firstname
* **lastname**: Lastname
* **email**: E-Mail address unique per user
* **street**: Street name & house number
* **city**: City
* **membership**: Membership status
* **workouts**: List of all Workouts of the user

#### Workouts
* **_id**: Unique number per workout
* **workout_type**: Activity type, eg: fitness walking, crosstrainer, rowing machine, spinning
* **date**: Start date of the activity
* **start_time**: Start time of the activity
* **end_time**: End time of the activity
* **calories**: Burnt calorie count
* **distance**: Distance in kilometers
* **comment**: Optional comment

#### Videos
* **_id**: Unique number per video
* **title**: Title of the video
* **desc**: Description of the video
* **length**: length of the video
* **path**: URL/Path to the video

## API Examples
### User Management:
**Retrieve list of users:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/users ```

**Retrieve a user:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/users/email=jbakkers@hotmail.com ```

**Create a user:**

``` curl -i -H "Content-Type: application/json" -X POST -d '{"firstname":"Jaap", "lastname":"Bakkers", "email":"jbakkers@hotmail.com", "street":"Tolseweg 22", "city":"Berghem", "membership":"premium"}' http://127.0.0.1:5000/api/v1/users ```

**Update a user:**

``` curl -i -H "Content-Type: application/json" -X PUT -d '{"name":"Jaapiene", "membership":"disabeld"}' http://127.0.0.1:5000/api/v1/users/email=jbakkers@outlook.com ```

**Delete a user:**

``` curl -i -H "Content-Type: application/json" -X DELETE localhost:5000/api/v1/users/email=jbakkers@hotmail.com ```


### Workout Management:
**Retrieve a list of workouts from a user:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/workouts/email=jbakkers@hotmail.com ```

**Retrieve a workout:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/workouts/[WORKOUT_ID] ```

**Create a workout:**

``` curl -i -H "Content-Type: application/json" -X POST -d '{"workout_type":"Walking", "date":"21-03-2019", "start_time":"14:02:21", "end_time":"15:04:23", "calories":"640", "distance":"3100", "comment":"Nice weather"}' http://127.0.0.1:5000/api/v1/workouts/user=jbakkers@hotmail.com ```

**Update a Workout:**

``` curl -i -H "Content-Type: application/json" -X PUT -d '{"calories":"6000"}' http://127.0.0.1:5000/api/v1/workouts/id=[WORKOUT_ID] ```

**Delete a workout:**

``` curl -i -H "Content-Type: application/json" -X DELETE localhost:5000/api/v1/workouts/id=[WORKOUT_ID] ```

### Video Management:
**Retrieve list of videos:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/videos/ ```

**Retrieve a video:**

``` curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/api/v1/videos/title=RunningForBeginners ```

**Create a video:**

``` curl -i -H "Content-Type: application/json" -X POST -d '{"title":"RunningForBeginners", "desc":"A instruction for beginners", "length":"30", "path":"https://azuredatabucket.mp4"}' http://127.0.0.1:5000/api/v1/videos/ ```

**Update a Video:**

``` curl -i -H "Content-Type: application/json" -X PUT -d '{"length":"60"}' http://127.0.0.1:5000/api/v1/videos/id=[VIDEO_ID] ```

**Delete a video:**

``` curl -i -H "Content-Type: application/json" -X DELETE localhost:5000/api/v1/videos/id=[VIDEO_ID] ```
