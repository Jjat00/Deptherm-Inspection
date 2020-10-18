from models.entities.User import User
from database.Storage import Storage

class UserDB():
    """
    docstring
    """
    def __init__(self):
        super(UserDB).__init__()
        self.storage = Storage()
        self.storage.getConnection()

    def getUserByID(self, ID):
        """
        Get user from database
        parameters:
            ID: id user
        return:
            user: object entity user 
        """
        query = "SELECT * FROM public.user WHERE ID=%i" % (ID)
        rows = self.storage.get(query)
        ID, userType, name, lastname, state, phone, email, password = rows[0]
        user = User(ID, userType, name, lastname,
                         state, phone, email, password)
        return user

    def insertUser(self, user):
        """
        Insert user into user db table 
        parameters:
            user: user type User class
        return:
            count: numbuer insert tuples
        """
        ID = user.getUserID()
        userType = user.getUserType()
        name = str(user.getName()).lower()
        lastname = str(user.getLastname())
        state = user.getState()
        phone = user.getCellphone()
        email = str(user.getEmail())
        password = user.getPassword()
        query = "INSERT INTO public.user(ID, userType, name, lastname, state, phone, email, password) VALUES(%i, %i, '%s', '%s', %r, %i, '%s', '%s')" % (
            ID, userType, name, lastname, state, phone, email, password)
        count = self.storage.insert(query)
        return count

    def updateUser(self):
        """
        docstring
        """
        pass


    def deleteUserByID(self, ID):
        """
        docstring
        """
        pass
