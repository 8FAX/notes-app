import json

def authenticate(username, password):
    with open('data/users.json', 'r') as f:
        users = json.load(f)

    for user in users:
        if (user['username'].upper() == username.upper() or user['email'].upper() == username.upper()) and user['password'] == password:
            return True
    return False