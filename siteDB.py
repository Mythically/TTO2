from pymongo import MongoClient
from secrets import compare_digest

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
