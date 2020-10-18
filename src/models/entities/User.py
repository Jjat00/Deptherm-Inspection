class User():
    """
    Model for User table
    """
    def __init__(self, userID, userType, name, lastname, state, cellphone, email, password):
        super(User).__init__()
        self.userID = userID
        self.userType = userType
        self.name = name
        self.lastname = lastname
        self.state = state
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

    def getLastname(self):
        return self.lastname

    def setLastname(self, lastname):
        self.lastname = lastname

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

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
            'userID': """ + str(self.userID) + """
            'userType': """ + str(self.userType) + """
            'name': '""" + str(self.name) + """'
            'lastname': '""" + str(self.lastname) + """'
            'state': """ + str(self.state) + """
            'password': '""" + str(self.password) + """'
            'cellphone': """ + str(self.cellphone) + """
            'email': '""" + str(self.email) + """'
        }"""
        return userStr
