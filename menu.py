import lol_SQL
import util
import champion
import user_SQL
while True:
    print("**********WELCOME TO LOL CHAMPION**********")
    print("1: Create Account")
    print("2: Login Account")
    print("3: Exit")
    choose = int(input("choose a option 1 , 2, 3: "))
    if choose > 3 or choose <= 0:
        continue

    if choose == 3:
        print('Good bye!')
        quit(0)
    elif choose == 1:
        id = util.isIdUserValid(input("Enter ID: "))
        name1 = util.isNameUserValid(input("Enter First Name : "))
        name2 = util.isNameUserValid(input("Enter Surname : "))
        password = util.isPassValid(input("Enter Password (> 10 characters): "))
        if id and name1 and name2 and password:
            name = str(name1) + " " + str(name2)
            user_SQL.addUser(id, name, password)


        else:
            print("Can not create account (Syntax error) ")
    elif choose == 2:
        name = util.isNameloginAccountValid(input("Please enter your account: "))
        password = util.isPassValid(input("Please enter a password: "))
        check = user_SQL.validUser(name,password)
        if check is False:
            print("Wrong account or password. Please check again")

        else:
            print("Logged in successfully")

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
                print("10: Battle result")
                print("11: Exit")
                action = int(input('choose a option[1..11]: '))
                if action > 11 or action <= 0:
                    continue

                if action == 11:
                    print('Good bye!')
                    quit(0)

                elif action == 1:
                    id = util.isIDvalid(input("Enter ID champion: "))
                    name = util.isNamevalid(input("Enter Name champion: "))
                    role = util.isRolevalid(input("Enter Role champion: "))
                    health = util.isHealthvalid(input("Enter Health champion: "))
                    attack = util.isAttackvalid(input("Enter Attack champion: "))
                    defense = util.isDefensevalid(input("Enter Defense champion: "))
                    attack_speed = util.isAttackSpeed(input("Enter Attack Speed champion: "))
                    if id and name and role and health and attack and defense:
                        lol_SQL.addChampionAttributesIntoTable(id, name, role, health, attack, defense, attack_speed)
                    else:
                        print("Can not add champion (Syntax error)")


                elif action == 2:
                    lol_SQL.displayTable()
                elif action == 3:
                    id = util.isIDvalid(input("Enter ID champion to delete: "))
                    if id:
                        lol_SQL.deleteVaribleIntoTable(id)
                    else:
                        print("Can not delete champion (Syntax error)")


                elif action == 4:
                    name = util.isNamevalid(input("Enter Name champion to delete: "))
                    if name:
                        lol_SQL.deleteChampion(name)
                    else:
                        print("Can not delete champion (Syntax error)")


                elif action == 5:
                    name1 = util.isNamevalid(input("Enter Name champion 1: "))
                    name2 = util.isNamevalid(input("Enter Name champion 2: "))

                    if name1 and name2:
                        lol_SQL.compareChampions(name1, name2)

                    else:
                        print("Can not find champion (Syntax error)")


                elif action == 6:
                    id = util.isIDvalid(input("Enter ID champion to update: "))
                    name = util.isNamevalid(input("Enter Name champion: "))
                    role = util.isRolevalid(input("Enter Role champion: "))
                    health = util.isHealthvalid(input("Enter Health champion: "))
                    attack = util.isAttackvalid(input("Enter Attack champion: "))
                    defense = util.isDefensevalid(input("Enter Defense champion: "))
                    attack_speed = util.isAttackSpeed(input("Enter Attack Speed champion: "))
                    if id and name and role and health and attack and defense and attack_speed:
                        lol_SQL.updateChampion(id, name, role, health, attack, defense, attack_speed)
                    else:
                        print("Can not update champion (Syntax error)")


                elif action == 7:
                    role = util.isRolevalid(input("Enter Role champion: "))
                    if role:
                        lol_SQL.displayRoleChampion(role)
                    else:
                        print("Can not find champion (Syntax error)")


                elif action == 8:
                    name = util.isNamevalid(input("Enter Name champion: "))
                    if name:
                        lol_SQL.searchChampion(name)
                    else:
                        print("Can not find champion (Syntax error)")
                # update action 9
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
                                lol_SQL.addChampionAttributesIntoTable(champion_id, champion_name, champion_role,
                                                                       champion_health,
                                                                       champion_attack, champion_defense,
                                                                       champion_attackSpeed)


                    except FileNotFoundError:
                        print('File not found')

                elif action == 10:
                    champions = []
                    view = "select * from Champion"
                    records = lol_SQL.fetch_all(view)
                    for record in records:
                        id = record[0]
                        name = record[1]
                        role = record[2]
                        health = record[3]
                        attack = record[4]
                        defense = record[5]
                        attack_speed = record[6]
                        champion = champion.Champion(id, name, role, health, attack, defense, attack_speed)
                        champions.append(champion)

                    result = util.champion_outcome(champions)
                    print(result)








