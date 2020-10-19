from models.entities.User import User
from database.Storage import Storage

class UserDB():
    """
    Services for user table db
    """
    def __init__(self):
        super(UserDB).__init__()
        self.storage = Storage()
        self.storage.connect()

    def getUserByID(self, ID):
        """
        Get user from database
        parameters:
            ID: id user
        return:
            user: object entity user 
        """
        try:
            query = "SELECT * FROM public.user WHERE ID=%i" % (ID)
            rows = self.storage.get(query)
            ID, userType, name, lastname, state, phone, email, password = rows[0]
            user = User(ID, userType, name, lastname,
                        state, phone, email, password)
        except IndexError:
            user = None

        return user

    def insertUser(self, user):
        """
        Insert user into user db table 
        parameters:
            user: user type User class
        return:
            count: number insert tuples
        """
        ID = user.getUserID()
        userType = user.getUserType()
        name = user.getName()
        lastname = user.getLastname()
        state = user.getState()
        phone = user.getCellphone()
        email = user.getEmail()
        password = user.getPassword()
        query = "INSERT INTO public.user(ID, userType, name, lastname, state, phone, email, password) VALUES(%i, %i, '%s', '%s', %r, %i, '%s', '%s')" % (
            ID, userType, name, lastname, state, phone, email, password)
        count = self.storage.insert(query)
        return count

    def updateUser(self, user):
        """
        Update user information in database
        parameters:
            user: user type User Class
        return:
            count: number insert tuples
        """
        ID = user.getUserID()
        userType = user.getUserType()
        name = user.getName()
        lastname = user.getLastname()
        state = user.getState()
        phone = user.getCellphone()
        email = user.getEmail()
        password = user.getPassword()
        query = "UPDATE public.user SET id=%i, usertype=%i, name='%s', lastname='%s', state=%r, phone=%i, email='%s', password='%s' WHERE ID='%i'" % (
            ID, userType, name, lastname, state, phone, email, password, ID)
        count = self.storage.insert(query)
        return count
        
    def deleteUserByID(self, ID):
        """
        Delete user from database by ID
        parameters:
            ID: id user 
        return:
            count: number insert tuples
        """
        query = "DELETE FROM public.user WHERE ID=%i" % (ID)
        count = self.storage.insert(query)
        return count

    def getUserByEmail(self, email, password):
        """
        Get user from database
        parameters:
            email, password: data access user
        return:
            user: object entity user 
        """
        try:
            query = "SELECT * FROM public.user WHERE (email='%s' AND password='%s')" % (email, password)
            rows = self.storage.get(query)
            ID, userType, name, lastname, state, phone, email, password = rows[0]
            user = User(ID, userType, name, lastname,
                        state, phone, email, password)
        except IndexError:
            user = None

        return user
