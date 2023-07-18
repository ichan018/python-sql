import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    
    return conn

def create_task(conn,task):
    sql = '''INSERT OR REPLACE INTO cars(id,make,model)
    VALUES(?,?,?)'''

    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()

    return cur.lastrowid

def main():
    database = r"C:\Users\ivans\source\repos\python sql\data.db"

    sql_create_cars_table = """ CREATE TABLE IF NOT EXISTS cars(
                                id integer PRIMARY KEY,
                                make text NOT NULL,
                                model text); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_cars_table)

        ifContinue = 1

        while ifContinue:
            print("What would you like to do?")
            print("0: End task")
            print("1: Enter a task")
            
            try:
                ans = int(input())
            except ValueError:
                print("Please only enter input.")
                continue

            if ans == 1:
                create_task(conn,(54678,'Honda','Passport'))
            elif ans == 0:
                print("Thanks for running this program")
                ifContinue = 0
    else:
        print("Error")


if __name__ == '__main__':
    main()
    