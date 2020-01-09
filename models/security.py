from models.user import User

def authenticate(username, password):
    user = User.find_user_name(username)
    if user and (user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_user_id(user_id)

