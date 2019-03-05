# MAF-api

## API Design
### API URIs
| HTTP Method | URL | Action |
| ------------- | ------------- | ------------- |
| GET | http://[hostname]/api/v1/users/ | Retrieve list of users |
| GET | http://[hostname]/api/v1/users/[user_id] | Retrieve a user |
| GET | http://[hostname]/api/v1/workouts/[workout_id] | Retrieve a workout |
| GET | http://[hostname]/api/v1/videos/ | Retrieve list of videos |
| GET | http://[hostname]/api/v1/videos/[video_id] | Retrieve a video |
| POST | http://[hostname]/api/v1/users/ | Create a user |
| POST | http://[hostname]/api/v1/workouts/ | Create a workout |
| POST | http://[hostname]/api/v1/videos/ | Create a video |
| DELETE | http://[hostname]/api/v1/users/[user_id] | Delete a user |
| DELETE | http://[hostname]/api/v1/workouts/[workout_id] | Delete a workout |
| DELETE | http://[hostname]/api/v1/videos/[video_id] | Delete a video |

### Fields
#### Users
* id: Unique number per user
* firstname: Firstname
* lastname: Lastname
* email: E-Mail address unique per user
* street: Street name & house number
* membership: Membership status

#### Workouts
* id: Unique number per workout
* type: Activity type, eg: fitness walking, crosstrainer, rowing machine, spinning
* date: Date of the activity
* start_time: Start time of the activity
* end_time: End time of the activity
* calories: Burnt calorie count
* distance: Distance in kilometers
* comment: Optional comment

#### Videos
* id: Unique number per video
* title: Title of the video
* desc: Description of the video
* path: URL/Path to the video