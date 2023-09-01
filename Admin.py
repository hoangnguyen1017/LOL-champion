import user
import user_SQL
import util
while True:
    print("********** User Account **********")
    print("1:Add User")
    print("2:Delete User ID")
    print("3:Update User")
    print("4:Exit")
    action = int(input("Choose a option 1...4: "))
    if action > 4 or action <= 0:
        continue

    if action == 4:
        print('Good bye!')
        quit(0)

    elif action == 1:
        id = util.isIdUserValid(input("Enter ID: "))
        name1 = util.isNameUserValid(input("Enter First Name : "))
        name2 = util.isNameUserValid(input("Enter Surname : "))
        password = util.isPassValid(input("Enter Password (> 10 characters): "))
        if id and name1 and name2 and password:
            name = str(name1) + " " + str(name2)
            user_SQL.addUser(id, name, password)
        else:
            print("Can not create account (Syntax error) ")
            
    elif action == 2:
        id = util.isIdUserValid(input("Enter ID User to delete: "))
        if id:
            user_SQL.deleteUser(id)
        else:
            print("Can not delete champion (Syntax error)")

    if action == 3:
        id = util.isIdUserValid(input("Enter ID to Update: "))
        name1 = util.isNameUserValid(input("Enter First Name : "))
        name2 = util.isNameUserValid(input("Enter Surname : "))
        password = util.isPassValid(input("Enter Password (> 10 characters): "))
        if id and name1 and name2 and password:
            name = str(name1) + " " + str(name2)
            user_SQL.updateUser(id, name, password)
        else:
            print("Can not update champion (Syntax error)")
