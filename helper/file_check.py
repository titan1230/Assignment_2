import os

def check_users():
    return os.path.exists("user_data/users.json")
