import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("Username already exists.\n")
    else:
        users[username] = hash_password(password)
        print("Created new user.\n")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful.\n")
    else:
        print("Invalid username or password.\n")

register("john", "password123")
login("john", "password123")
login("john", "password456")
login("jane", "password123")