import sqlite3


conn = sqlite3.connect('lolchampion.db')
cursor = conn.cursor()

def addUser(id,name,password):
    view = "select * from User where id = ?"
    add = """INSERT INTO User
                                              (id,name,password)
                                              VALUES (?, ?, ?);"""
    if fetch_one(view, (id,)) is not None:
        print("ID is not available")
    elif fetch_one(view, (id,)) is None:
        execute_sql(add, (id,name,password))
        print("Account successfully created")
    else:
        print("Can not create account (Syntax error) ")


def deleteUser(id):
    view = "select * from User where id = ?"
    if fetch_one(view, (id,)) is not None:
        dele = """DELETE from User where id = ?"""
        execute_sql(dele,(id))
        print("Delete user successful")
    else:
        print("ID is not available")

def updateUser(id,name,password):
    view = "select * from User where id = ?"
    update = """Update  User Set name = ? , password = ? Where id = ?"""
    if fetch_one(view, (id,)) is not None:
        execute_sql(update,(name,password,id))
        print("Record updated successfully")
    else:
        print("Can not find User")

def validUser(name,password):
    view = "select * from User where name = ? and password = ?"
    if fetch_one(view, (name, password,)) is None:
        return False
    else:
        return True












def execute_sql(sql, params=()):
   cur = conn.cursor()
   cur.execute(sql, params)
   conn.commit()
   return cur

def fetch_all(sql):
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def fetch_all1(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchall()

def fetch_one(sql, params=()):
    cur = conn.cursor()
    cur.execute(sql, params)
    return cur.fetchone()

def executemany_sql(sql, params):
    cur = conn.cursor()
    cur.executemany(sql, params)
    conn.commit()
    return cur