# Backend

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

## Reset migrations

1. Change the model in models.py
2. Remove migrations folder
3. Drop the Database / Delete db.sqlite3
4. python3 manage.py makemigrations <app_name>
5. python3 manage.py migrate
6. If added a new Model, change serializer.py
7. Make sure URL exists and views function exists

## TODO

1. Change models.py to recieve and format all the data fields for the app
2.
