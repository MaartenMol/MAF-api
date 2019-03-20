# MAF-api

## API Design
### API URIs
| Implemented | HTTP Method | URL | Action |
| ------------- | ------------- | ------------- | ------------- |
| [x] | GET | http://[hostname]/api/v1/users/ | Retrieve list of users |
| [x] | GET | http://[hostname]/api/v1/users/[searchField]/[searchTerm] | Retrieve a user |
|  | GET | http://[hostname]/api/v1/workouts/[workout_id] | Retrieve a workout |
| [x] | GET | http://[hostname]/api/v1/videos/ | Retrieve list of videos |
| [x] | GET | http://[hostname]/api/v1/videos/[video_id] | Retrieve a video |
| [x] | POST | http://[hostname]/api/v1/users/ | Create a user |
|  | POST | http://[hostname]/api/v1/workouts/ | Create a workout |
| [x] | POST | http://[hostname]/api/v1/videos/ | Create a video |
| [x] | PUT | http://[hostname]/api/v1/users/email/[email] | Update a User |
| [x] | PUT | http://[hostname]/api/v1/videos/id/[id] | Update a User |
| [x] | DELETE | http://[hostname]/api/v1/users/email/[email] | Delete a user |
|  | DELETE | http://[hostname]/api/v1/workouts/[workout_id] | Delete a workout |
| [x] | DELETE | http://[hostname]/api/v1/videos/[video_id] | Delete a video |

### Fields
#### Users
* **_id**: Unique number per user
* **firstname**: Firstname
* **lastname**: Lastname
* **email**: E-Mail address unique per user
* **street**: Street name & house number
* **city**: City
* **membership**: Membership status

#### Workouts
* **_id**: Unique number per workout
* **type**: Activity type, eg: fitness walking, crosstrainer, rowing machine, spinning
* **date**: Date of the activity
* **start_time**: Start time of the activity
* **end_time**: End time of the activity
* **calories**: Burnt calorie count
* **distance**: Distance in kilometers
* **comment**: Optional comment

#### Videos
* **_id**: Unique number per video
* **title**: Title of the video
* **desc**: Description of the video
* **path**: URL/Path to the video
