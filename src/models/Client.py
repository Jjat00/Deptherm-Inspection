class Client():
    """
    model for table client
    """
    def __init__(self, name: str, lastname: str, email: str, cel: str):
        super(Client).__init__()
        self.name = name
        self.lastname = lastname
        self.email = email
        self.cel = cel

    def getName(self):
        """
        docstring
        """
        return self.name

    def setName(self, name: str):
        """
        docstring
        """
        self.name = name

