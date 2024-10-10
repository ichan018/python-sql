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
        conn.commit()        
    except Error as e:
        print(e)
    
    return conn

def create_task(conn,task):
    sql = "INSERT OR REPLACE INTO vehicles(system_id,id,make,model) VALUES(?,?,?,?)"

    cur = conn.cursor()
    cur.execute(sql,task)
    conn.commit()

    return cur.lastrowid

def get_info(conn):
    car_id = input("Enter car number id: ")
    car_make = input("Enter car make: ")
    car_model = input("Enter car model: ")

    cur = conn.cursor()
    sql = '''SELECT system_id
             FROM vehicles
             WHERE system_id = (SELECT MAX(system_id) FROM vehicles);'''
    sys_id_info = cur.execute(sql)
    if sys_id_info:
        sys_id_list = []
        #while appending sys_id check for max id
        max_id = 1
        for x in sys_id_info:
            sys_id_tuple = x
            sys_id_curr = "" #store characters of tuple
            for i in sys_id_tuple:
                sys_id_curr += str(i)
            sys_id_curr = int(sys_id_curr)

            if sys_id_curr > max_id:
                max_id = sys_id_curr
            sys_id_list.append(x)
        sys_id = max_id + 1
        #max_sys_id = sys_id_list[0] # fix
        #sys_id = int(str(max_sys_id)) + 1 #fix
    else:
        sys_id = 1
        
    return (sys_id,car_id,car_make,car_model)

def read_list(conn):
    sql = "SELECT * FROM vehicles"
    cur = conn.cursor()
    x = cur.execute(sql)
    
    for row in x.fetchall():
        print(row)
    
def delete_info(conn,system_id_info):
    #print("Working on it")
    confirmDelete = input("Type 'y' to confirm that you would like to delete: ")
    if confirmDelete == "y":
        cur = conn.cursor()
        x = cur.execute("DELETE FROM vehicles WHERE system_id = ?",system_id_info)
        print("Your list is now: ")
        read_list(conn)
    else:
        print(val,"not deleted")

def main():
    database = r"C:\Users\ivans\source\repos\python sql\vehicle_data.db"

    sql_create_cars_table = """ CREATE TABLE IF NOT EXISTS vehicles (
                                system_id int PRIMARY KEY,
                                id text,
                                make text NOT NULL,
                                model text); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_cars_table)

        ifContinue = 1
        highestNum = 3

        while ifContinue:
            print("What would you like to do?")
            print("0: End program")
            print("1: Enter a task")
            print("2: Delete id")
            print("3: Print table")
            
            try:
                ans = int(input())
            except ValueError:
                print("Please only enter input.")
                continue

            if ans == 3:
                read_list(conn)
            elif ans ==2:
                val = input("Enter system_id (not id) of vehicle you would like to delete: ")

                delete_info(conn,(val,))
            elif ans == 1:
                car_params = get_info(conn)
                create_task(conn,car_params)
            elif ans == 0:
                print("Thanks for running this program!")
                ifContinue = 0
            else:
                print("Error: Enter a number between 0 and " + str(highestNum) + ".")
    else:
        print("Error")


if __name__ == '__main__':
    main()
    