from flask import Flask, request

users = [ {"id": 1, "username": "hodi", "password": "123", "salary": 5000, "address": "123 Main St", "active": True},
{"id": 2, "username": "josh", "password": "456", "salary": 60000, "address": "456 Oak St",
"active": False},]

app = Flask(__name__)

#Retrieve a list of all users
@app.get('/users')
def get_users():
    return users

#Retrieve a user by ID
@app.get('/users/<int:user_id>')
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return 'data not found', 400

#Create a new user
@app.post('/users')
def post_user():
    user = request.json
    user['id'] = user[-1]['id']+1
    users.append(user)
    return users

#Update a user by ID
@app.put('/users/<int:user_id>')
def update_user(user_id):
    new_user = request.json
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            users.pop(i)
            users.insert(i, new_user)
    return users

#Delete a user by ID
@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
    return 'Done'

#Delete all users
@app.delete('/users')
def delete_all_users():
    users.clear()
    return users