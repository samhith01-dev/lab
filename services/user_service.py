users = []

def create_user(data):
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return new_user

def get_users():
    return users