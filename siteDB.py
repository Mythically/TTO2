from pymongo import MongoClient
from secrets import compare_digest

myclient = MongoClient("mongodb://localhost:27017/")
siteDB = myclient["siteDatabase"]
logins = siteDB['logins']


def logout(username):
    u = {'username': f'{username}'}
    sets = {"$set": {"loggedin": "False"}}
    logins.update_one(u, sets)


def login(username, password):
    if checkLogin(username, password):
        u = {'username': f'{username}'}
        sets = {"$set": {"loggedin": "True"}}
        logins.update_one(u, sets)
    else:
        return False


def checkIfLoggedIn(username):
    print("checking")
    try:
        login_name = logins.find({'username': f'{username}'})
        if login_name[0]['loggedin'] == True:
            print("true")
            return True
        else:
            print("false")
            return False
    except TypeError as e:
        print(e)
        return "An error has occured, please try again!"


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
    try:
        login_name = logins.find({'username': f'{username}'})
    except IndexError as e:
        print(e)
        return False
    if login_name[0]['username'] == username:
        if compare_digest(login_name[0]['password'], password):
            print("DB: Logged in")
            return True
        else:
            print("DB: Wrong Credentials")
            return False
    else:
        print("DB: Not registered")
        return False

