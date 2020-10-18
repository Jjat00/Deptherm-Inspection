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
    docstring
    """
    user = User(1088597620, 1, 'Jhon', 'Valencia', True, 3454277865, 'juan@gmail.com', '151355')
    count = userDB.insertUser(user)
    print(count)
