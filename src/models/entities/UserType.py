class UserType():
    """
    Model for User type table
    """
    def __init__(self, id, name):
        super(UserType).__init__()
        self.userTypeID = id
        self.name = name

    def getUserTypeID(self):
        return self.userTypeID

    def setUserTypeID(self, userTypeID):
        self.userTypeID = userTypeID

    def getName(self):
        return self.name

    def toString(self):
        userStr = """ userType: {
            "userTypeID": """ + str(self.userTypeID) + """
            "nameUserType": """ + str(self.name) + """
        }"""
        return userStr
