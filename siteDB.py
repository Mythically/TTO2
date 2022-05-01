from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
siteDB = myclient["siteDatabase"]
logins = siteDB['logins']


def checkIfRegistered(username):
    try:
        login_name = logins.find({'username': f'{username}'})
        if login_name[0]['username'] == username:
            return True
        else:
            return False
    except TypeError as e:
        print(e)
        return "An error has occured, please try again!"


def insertLogin(username, passowrd):
    try:
        logins.insert_one({'username': f'{username}', 'password': f'{passowrd}'})
        return "You are now registered"
    except Exception as e:
        print(e)
        return "An error has occured, please try again"

def checkLogin(username, password):
    login_name = logins.find({'username': f'{username}'})
    if login_name[0]['username'] == username:
        if login_name[0]['password'] == password:
            return True
        else:
            return False
    else:
        return False

# print(checkIfRegistered("TheMythh"))
print(checkLogin("TheMythh", "admin"))