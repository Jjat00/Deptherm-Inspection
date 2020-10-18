from models.entities.User import User
from models.interfaces.UserDB import UserDB

userDB = UserDB()

def selectUserDB():
    """
    get user from database
    """
    user = userDB.getUserByID(1088597617)
    print(user.toString())
    

def insertUserDB():
    """
    insert user
    """
    user = User(1088597620, 1, 'Jhon', 'Valencia', True, 3454277865, 'juan@gmail.com', '151355')
    count = userDB.insertUser(user)
    print(count)

def updatetUserDB():
    """
    update user
    """
    user = User(1088597620, 1, 'Jhon', 'Valencia', True, 3454277865, 'juan@gmail.com', '151355')
    count = userDB.updateUser(user)
    print(count)

def deleteUser():
    """
    delete user
    """
    count = userDB.deleteUserByID(1085897621)
