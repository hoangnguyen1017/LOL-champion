import sqlite3


conn = sqlite3.connect('lolchampion.db')
cursor = conn.cursor()


def addChampionAttributesIntoTable(id,name,role,health,attack,defense,attack_speed):
    view = "select * from Champion where id = ?"
    insert = """INSERT INTO Champion
                                              (id,name,role,health,attack,defense,attack_speed)
                                              VALUES (?, ?, ?, ?, ?, ?, ? );"""


    if fetch_one(view, (id,)) is not None:
        print("id is not available")
    elif fetch_one(view, (id,)) is None:
        execute_sql(insert, (id,name,role,health,attack,defense,attack_speed))
        print("Record add Champion successfully")
    else:
        print("Can not add champion")


def deleteVaribleIntoTable(id):
    view = "select * from Champion where id = ?"
    if fetch_one(view, (id,)) is not None:
        delete = """DELETE from Champion where id = ?"""
        execute_sql(delete,(id,))

        print("Record delete successfully ")
    else:
        print("Not found the ID")
def deleteChampion(name):
    view = "select * from Champion where name = ?"
    if fetch_one(view, (name,)) is not None:
        delete = """DELETE from Champion where name = ?"""
        execute_sql(delete, (name,))

        print("Record delete successfully ")
    else:
        print("Not found the ID")
def updateChampion(id,name,role,health,attack,defense,attack_speed):
    view = "select * from Champion where id = ?"
    update = """ UPDATE Champion SET name = ?, role = ?, health = ?, attack = ?, defense = ?, attack_speed = ? WHERE id = ? """
    if fetch_one(view,(id,)) is not None:
        execute_sql(update,(name,role,health,attack,defense,attack_speed, id))
        print("Record updated successfully")
    else:
        print("Champion not found")

def displayTable():
    view = "select * from Champion"
    records = fetch_all(view)
    for record in records:
        print("Id = ", record[0])
        print("Name = ", record[1])
        print("Role = ", record[2])
        print("Health = ", record[3])
        print("Attack = ", record[4])
        print("Defense  = ", record[5])
        print("-------------------", "\n")
def displayRoleChampion(role):
    view = "select * from Champion where role =  ?"
    records1 = fetch_all1(view,(role,))
    if records1:
        for record1 in records1:
            print("Id = ", record1[0])
            print("Name = ", record1[1])
            print("Role = ", record1[2])
            print("Health = ", record1[3])
            print("Attack = ", record1[4])
            print("Defense  = ", record1[5])
            print("-------------------", "\n")
    else:
        print("Champion not found")
def searchChampion(name):
    view = "select * from Champion where name =  ?"
    records2 = fetch_all1(view, (name,))
    if records2:
        for record2 in records2:
            print("Id = ", record2[0])
            print("Name = ", record2[1])
            print("Role = ", record2[2])
            print("Health = ", record2[3])
            print("Attack = ", record2[4])
            print("Defense  = ", record2[5])
            print("-------------------", "\n")
    else:
        print("Champion not found")


def compareChampions(name1, name2):
    view = "SELECT * FROM Champion WHERE name IN (?, ?)"
    champions = fetch_all1(view, (name1, name2))

    if len(champions) == 2:
        champion1 = champions[0]
        champion2 = champions[1]

        print("Champion 1:")
        print("Id = ", champion1[0])
        print("Name = ", champion1[1])
        print("Role = ", champion1[2])
        print("Health = ", champion1[3])
        print("Attack = ", champion1[4])
        print("Defense = ", champion1[5])
        print("-------------------", "\n")

        print("Champion 2:")
        print("Id = ", champion2[0])
        print("Name = ", champion2[1])
        print("Role = ", champion2[2])
        print("Health = ", champion2[3])
        print("Attack = ", champion2[4])
        print("Defense = ", champion2[5])
        print("-------------------", "\n")

        print("Champion 1 ----- Champion 2")
        if int(champion1[3]) > int(champion2[3]):
            print("Health: %d > %d" % (champion1[3], champion2[3]))
        elif int(champion1[3]) < int(champion2[3]):
            print("Health: %d < %d" % (champion1[3], champion2[3]))
        else:
            print("Health: %d = %d" % (champion1[3], champion2[3]))

        if int(champion1[4]) > int(champion2[4]):
            print("Attack: %d > %d" % (champion1[4], champion2[4]))
        elif int(champion1[4]) < int(champion2[4]):
            print("Attack: %d < %d" % (champion1[4], champion2[4]))
        else:
            print("Attack: %d = %d" % (champion1[4], champion2[4]))

        if int(champion1[5]) > int(champion2[5]):
            print("Defense: %d > %d" % (champion1[5], champion2[5]))
        elif int(champion1[5]) < int(champion2[5]):
            print("Defense: %d < %d" % (champion1[5], champion2[5]))
        else:
            print("Defense: %d = %d" % (champion1[5], champion2[5]))
    else:
        print("Champion not found")



def execute_sql(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return cur

def fetch_all(sql):
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()
def fetch_all1(sql,params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()
def fetch_one(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchone()



def executemany_sql( sql, params):

    cur = conn.cursor()
    cur.executemany(sql, params)
    conn.commit()
    return cur



