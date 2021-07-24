class Account:
    def __init__(self,name,password,mail):
        self.name = name
        self.password = password
        self.mail = mail
    
    def getName(self):
        return self.name

    def getPassword(self):
        return self.password
    
    def getMail(self):
        return self.mail
