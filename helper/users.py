import json

def load_user_data():
    with open('user_data/users.json', 'r') as file:
        return json.load(file)
    
def login_user(username, password):
    users = load_user_data()
        
    if username in users and users[username]["password"] == password:
        return users[username]
    return False
    print("Keyboard Interrupted")


def register_user(username, password, name, email):
    users = load_user_data()
    
    if username in users:
        return False
    
    users[username] = {
        "name": name,
        "username": username,
        "email": email,
        "password": password
    }
    
    with open('user_data/users.json', 'w') as file:
        json.dump(users, file)
    return users[username]

def check_user_exists(username):
    users = load_user_data()
    if username in users:
        return True
    return False