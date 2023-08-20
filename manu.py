import lol
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

def isIDvalid(input):
    if input.isdigit():
        return input
    else:
        print("The ID format must be a number")

def isNamevalid(input):
    if input.isalpha():
        return input
    else:
        print("The Name format must be character")
def isRolevalid(input):
    if input.isalpha():
        return input
    else:
        print("The Role format must be character")
def isHealthvalid(input):
    if input.isdigit():
        return input
    else:
        print("The Heal format must be a number")
def isAttackvalid(input):
    if input.isdigit():
        return input
    else:
        print("The Attack format must be a number")
def isDefensevalid(input):
    if input.isdigit():
        return input
    else:
        print("The Defense format must be a number")
def isAttackSpeed(input):
    if ('.' in input):
        f, l = input.split('.')
        if f.isdigit() and l.isdigit():
            return input
    else:
        print("The Attack Speed format must be a decimal")


while True:
    print("**********MENU**********")
    print("1:Add champion")
    print("2:Display the list of champion")
    print("3:Delete champion")
    print("4:Delete champion base on name")
    print("5:Compare two champions (based on health, attack and defense)")
    print("6:Update champion")
    print("7:Display the champion have same role")
    print("8:Search the champion (name)")
    print("9:Open file infor champion")
    print("10: Exit")
    action = int(input('choose a option[1..10]: '))
    if action > 10 or action <= 0:
        continue

    if action == 10:
        print('Good bye!')
        quit(0)

    elif action == 1:
        id = isIDvalid(input("Enter ID champion: "))
        name = isNamevalid(input("Enter Name champion: "))
        role = isRolevalid(input("Enter Role champion: "))
        health = isHealthvalid(input("Enter Health champion: "))
        attack = isAttackvalid(input("Enter Attack champion: "))
        defense = isDefensevalid(input("Enter Defense champion: "))
        attack_speed = isAttackSpeed(input("Enter Attack Speed champion: "))
        if id and name and role and health and attack and defense and attack_speed:
            lol.addChampionAttributesIntoTable(id, name, role, health, attack, defense,attack_speed)
        else:
            print("Can not add champion (Syntax error)")


    elif action == 2:
        lol.displayTable()
    elif action == 3:
        id = isIDvalid(input("Enter ID champion to delete: "))
        if id:
            lol.deleteVaribleIntoTable(id)
        else:
            print("Can not delete champion (Syntax error)")


    elif action == 4:
        name = isNamevalid(input("Enter Name champion to delete: "))
        if name:
            lol.deleteChampion(name)
        else:
            print("Can not delete champion (Syntax error)")


    elif action == 5:
        name1 = isNamevalid(input("Enter Name champion 1: "))
        name2 = isNamevalid(input("Enter Name champion 2: "))
        if name1 and name2:
            lol.compareChampions(name1,name2)

        else:
            print("Can not find champion (Syntax error)")


    elif action == 6:
        id = isIDvalid(input("Enter ID champion to update: "))
        name = isNamevalid(input("Enter Name champion: "))
        role = isRolevalid(input("Enter Role champion: "))
        health = isHealthvalid(input("Enter Health champion: "))
        attack = isAttackvalid(input("Enter Attack champion: "))
        defense = isDefensevalid(input("Enter Defense champion: "))
        attack_speed = isAttackSpeed(input("Enter Attack Speed champion: "))
        if id and name and role and health and attack and defense and attack_speed:
            lol.updateChampion(id,name,role,health,attack,defense,attack_speed)
        else:
            print("Can not update champion (Syntax error)")


    elif action == 7:
        role = isRolevalid(input("Enter Role champion: "))
        if role:
            lol.displayRoleChampion(role)
        else:
            print("Can not find champion (Syntax error)")


    elif action == 8:
        name = isNamevalid(input("Enter Name champion: "))
        if name:
            lol.searchChampion(name)
        else:
            print("Can not find champion (Syntax error)")
    #update action 9
    elif action == 9:

        file_name = input('Enter a file: ')
        try:
            with open(file_name, "r") as csv_file:
                reader = csv_file.readlines()
                for line in reader:
                    attr = line.strip().split(',')
                    champion_id = attr[0]
                    champion_name = attr[1]
                    champion_role = attr[2]
                    champion_health = attr[3]
                    champion_attack = attr[4]
                    champion_defense = attr[5]
                    champion_attackSpeed = attr[6]
                    lol.addChampionAttributesIntoTable(champion_id, champion_name, champion_role, champion_health,
                                                           champion_attack, champion_defense, champion_attackSpeed)


        except FileNotFoundError:
            print('File not found')
