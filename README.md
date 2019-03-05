# MAF-api

## API Design
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