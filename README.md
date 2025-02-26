# Backend

## Implementaion

This repo contains the User and Admin side Backend that is to be used for the application. The user, when first entering, will register using their google account / whatever the frontend seems fit and the Backend will recieve the userProfile in one json call.

While registering, if the user enters "\_admin\_" anywhere in their username, they will be marked as admin and during Login the next time, they will be able to login using only Admin login.

## DataBase Formats

### User Profile

1. Registration Number (Unique)
2. Name
3. Email
4. Hostel
5. Block
6. Phone Number
7. Admin (Boolean)

### Form Data

1. Registration Number
2. Name
3. Domains

## Routes

### Send data for new register

curl -X POST http://127.0.0.1:8000 -H "Content-Type: application/json" -d '**_Enter JSON Format here_**'

### Get list of all data

curl -X GET http://127.0.0.1:8000 -H "Content-Type: application/json"

### Check specific registration number

curl -X GET http://127.0.0.1:8000/check/ **_Registration Number_** -H "Content-Type: application/json"

### Delete all data

curl -X DELETE http://127.0.0.1:8000/delete -H "Content-Type: application/json"

### Delete specific registration number

curl -X DELETE http://127.0.0.1:8000/delete/ **_Registration Number_** -H "Content-Type: application/json"

### Edit entire profile

curl -X PUT http://127.0.0.1:8000/edit/ **_Registration Number_** -H "Content-Type: application/json" -d '**_Enter JSON Format here_**'

### Edit specific fields of a profile

curl -X PATCH http://127.0.0.1:8000/edit/ **_Registration Number_** -H "Content-Type: application/json" -d '**_Enter JSON Format here_**'

### Upload Form submission by a student

curl -X POST http://127.0.0.1:8000/upload -H "Content-Type: application/json" -d '**_Enter JSON Format here_**'

### Recieve list of all Form submissions

curl -X GET http://127.0.0.1:8000/upload -H "Content-Type: application/json"

## Reset migrations

1. Change the model in models.py
2. Remove migrations folder
3. Drop the Database / Delete db.sqlite3
4. python3 manage.py makemigrations <app_name>
5. python3 manage.py migrate
6. If added a new Model, change serializer.py
7. Make sure URL exists and views function exists

## TODO

1. Automatically Delete the NightSlip form data at Midnight
2.
