class Champion:
    def __init__(self, id="", name="", role="", health="", attack="", defense="", attackSpeed=""):
        self.id = id
        self.name = name
        self.role = role
        self.health = health
        self.attack = attack
        self.defense = defense
        self.attackSpeed = attackSpeed


    def __str__(self):
        return self.id + ","+self.name+","+self.role+"," + self.health+"," + self.attack+","+self.defense+ ","+ self.attackSpeed+","