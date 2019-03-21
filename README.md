# MAF-api

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
| :heavy_check_mark: | GET | http://[hostname]/api/v1/workouts/[workout_id] | Retrieve a workout |
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
