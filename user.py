class User:
    def __init__(self, id="", name="", password=""):
        self.id = id
        self.name = name
        self.password = password



    def __str__(self):
        return self.id + ","+self.name+","+self.password+","