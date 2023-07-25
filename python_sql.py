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

def get_info():
    car_id = int(input("Enter car number id"))
    car_make = input("Enter car make")
    car_model = input("Enter car model")

    return (car_id,car_make,car_model)

def read_list(conn):
    sql = '''SELECT * FROM cars'''
    cur = conn.cursor()
    x = cur.execute(sql)
    
    for row in x.fetchall():
        print(row)
    
def delete_info(conn,modelInfo):
    #print("Working on it")
    confirmDelete = input("Type 'y' to confirm that you would like to delete")
    if confirmDelete == "y":
        sql = '''DELETE FROM cars WHERE model = VALUES(?)'''
        cur = conn.cursor()
        x = cur.execute(sql)
    else:
        print(val,"not deleted")

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
            print("2: Delete information")
            print("3: Print table")
            
            try:
                ans = int(input())
            except ValueError:
                print("Please only enter input.")
                continue

            if ans == 3:
                read_list(conn)
            if ans ==2:
                val = input("Enter model of vehicle you would like to delete")

                delete_info(conn,(val))
            elif ans == 1:
                car_params = get_info() #work on it
                create_task(conn,car_params)
            elif ans == 0:
                print("Thanks for running this program")
                ifContinue = 0
    else:
        print("Error")


if __name__ == '__main__':
    main()
    