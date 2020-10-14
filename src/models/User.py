class User():
    """
    Model for User table
    """
    def __init__(self, userID, userType, name, password, cellphone, email):
        super(User).__init__()
        self.userID = userID
        self.userType = userType
        self.name = name
        self.password = password
        self.cellphone = cellphone
        self.email = email

    def getUserID(self):
        return self.userID

    def setUserID(self, userID):
        self.userID = userID

    def getUserType(self):
        return self.userType

    def setUserType(self, userType):
        self.userType = userType

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getCellphone(self):
        return self.cellphone

    def setCellphone(self, cellphone):
        self.cellphone = cellphone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def toString(self):
        userStr = """ user: {
            "userID": """ + str(self.userID) + """
            "userType": """ + str(self.userType) + """
            "name": """ + str(self.name) + """
            "password": """ + str(self.password) + """
            "cellphone": """ + str(self.cellphone) + """
            "email": """ + str(self.email) + """
        }"""
        return userStr
