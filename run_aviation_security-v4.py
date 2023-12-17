import mysql.connector
import time
import os
from datetime import datetime
import csv
from colorama import Fore, Style


# Define mydb as a global variable
mydb = None

# Define Menu() Screen
def menu_screen():
    print("+-----------------------------------------------------------------------------------------------------------------------+")
    print("|                                             INSTRUCTIONS                                                              |")
    print("|                                             ------------                                                              |")
    print("|                                                                                                                       |")
    print("| COMMANDS FOR DATABASE MANIPULATION:                                                                                   |")
    print("|                                                                                                                       |")
    print("| use database;      > To use a database.                     #working                                                  |")
    print("| show databases;    > To show all databases.                 #working                                                  |") 
    print("| create database;   > To create a new database.              #working                                                  |")
    print("| delete database;   > To delete an existing database.        #working                                                  |")
    print("|                                                                                                                       |")
    print("|_______________________________________________________________________________________________________________________|")
    print("|                                                                                                                       |")
    print("| COMMANDS FOR TABLE MANIPULATION:                                                                                      |")
    print("|                                                                                                                       |")
    print("| show tables;       > To show tables in a database.                               #working                             |") 
    print("| create table;      > To create a new table.                                      #working                             |")
    print("| describe table;    > To see the schema (structure) of a table.                   #working                             |")
    print("| delete a table;    > To remove/drop a table completely along with it's content   #working                             |")
    print("| drop table;        > To delete all records from table completely.                #working                             |")
    print("|                                                                                                                       |")
    print("|_______________________________________________________________________________________________________________________|")
    print("|                                                                                                                       |")
    print("| COMMANDS FOR COLUMN MANIPULATION:                                                                                     |")
    print("|                                                                                                                       |")
    print("| add column;        > To add a new column to an existing table.                  #working                              |")
    print("| modify column;     > To change the data type of a column in a table.            #working                              |")
    print("| delete column;     > To delete an existing column in a table.                   #working                              |")
    print("|                                                                                                                       |")
    print("|_______________________________________________________________________________________________________________________|")
    print("| COMMANDS FOR IN-TABLE MANIPULATION:                                                                                   |")
    print("|                                                                                                                       |")
    print("| insert;            > To insert data into a table.                                       #working                      |")
    print("| update;            > To modify or change the value of a data item in a column/field.    #notworking                   |")
    print("| delete;            > To delete row(s)/record(s).   #                                    #ncheck                       |")
    print("|                                                                                                                       |")
    print("|_______________________________________________________________________________________________________________________|")
    print("|                                                                                                                       |")
    print("| COMMANDS FOR CUSTOM AND ADVANCES FUNCTIONS:                                                                           |")
    print("|                                                                                                                       |")
    print("| custom;            > To use custom additional commands.                                 #working                      |")
    print("|_______________________________________________________________________________________________________________________|")
    print("|                                                                                                                       |")
    print("| COMMANDS FOR SELECTION                                                                                                |")
    print("|                                                                                                                       |")
    print("| select;            > To select custom data from a table without any arguements          #working                      |")
    print("| select*;           > To select all data from a table                                    #working                      |")
    print("|_______________________________________________________________________________________________________________________|")
    print("|                                                                                                                       |")
    print("|                                                                                                                       |")
    print("| COMMAND TO EXIT :                                                                                                     |")
    print("|                                                                                                                       |")
    print("| exit; > To exit          #working                                                                                     |")
    print("|                                                                                                                       |")
    print("+-----------------------------------------------------------------------------------------------------------------------+")

# Define clear screen function
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  
# Defining Logo artwork
def popo_logo():
  print('''
  .______     ______   .______     ______           ___       __  .______     ____    __    ____  ___   ____    ____  _______.
  |   _  \   /  __  \  |   _  \   /  __  \         /   \     |  | |   _  \    \   \  /  \  /   / /   \  \   \  /   / /       |
  |  |_)  | |  |  |  | |  |_)  | |  |  |  |       /  ^  \    |  | |  |_)  |    \   \/    \/   / /  ^  \  \   \/   / |   (----`
  |   ___/  |  |  |  | |   ___/  |  |  |  |      /  /_\  \   |  | |      /      \            / /  /_\  \  \_    _/   \   |
  |  |      |  `--'  | |  |      |  `--'  |     /  _____  \  |  | |  |\  \----.  \    /\    / /  _____  \   |  | .----)   |
  | _|       \______/  | _|       \______/     /__/     \__\ |__| | _| `._____|   \__/  \__/ /__/     \__\  |__| |_______/
  ''')

#----------------------------------------------------------------------------

# Define show database function                          #function_working           #debugged
def show_database():
  print()
  print("Sorry!, You do not have the permissions to view databases")
  print()

# Define connect to database function                    #function_working            #debugged
def connect_to_database():
  global mydb  # Use the global mydb variable

  for tries in range(3):
    username = "freedb_admin_user-neelaksh"
    password = "ZF#DrDKQwvas4U!"
    databasename = "freedb_informatics_school-project"
    hostname = "sql.freedb.tech"

    cursor = None

    try:
      mydb = mysql.connector.connect(host=hostname,
                                     user=username,
                                     passwd=password,
                                     database=databasename)
      cursor = mydb.cursor()
      print("Connected to the database " + Fore.GREEN + "successfully!" +
            Style.RESET_ALL)
      time.sleep(2)
      clear_screen()
      time_now = datetime.now()
      print(f"\nLOGGED IN AS: {username}@{hostname}")
      print(f"TIME: {time_now.strftime('%H:%M:%S %p')}")
      print(f"\nMySQL server version: {mydb.get_server_info()}")

      # Call the popo_logo() function to show logo
      popo_logo()

      # Call the menu_screen() function to show menu screen
      menu_screen()
      break
    except mysql.connector.Error as err:
      print(f"Error connecting to the database: {err}")
      if tries == 2:
        print("You have exceeded the number of tries. Exiting program.")
        exit()
    finally:
      if cursor:
        cursor.close()

# Define reconnect to database function
def reconnect_to_database():                             #function_working            #debugged
  for tries in range(3):
    username = "freedb_admin_user-neelaksh"
    password = "ZF#DrDKQwvas4U!"
    databasename = "freedb_informatics_school-project"
    hostname = "sql.freedb.tech"

    cursor = None

    try:
      mydb = mysql.connector.connect(host=hostname,
                                     user=username,
                                     passwd=password,
                                     database=databasename)
      cursor = mydb.cursor()
      print("Connected to the database " + Fore.GREEN + "successfully!" + Style.RESET_ALL)
      time.sleep(2)
      print("Reconnected to database " + Fore.GREEN + "successfully!" + Style.RESET_ALL)
      time_now = datetime.now()
      print(f"\nLOGGED IN AS: {username}@{hostname}")
      print(f"TIME: {time_now.strftime('%H:%M:%S %p')}")
      print(f"\nMySQL server version: {mydb.get_server_info()}")
      break
    except mysql.connector.Error as err:
      print(f"Error connecting to the database: {err}")
      if tries == 2:
        print("You have exceeded the number of tries. Exiting program.")
        exit()
    finally:
      if cursor:
        cursor.close()

# Define Show Databases(), default to show error
def nopermission():                                      #function_working           #debugged
    print()
    print("You do not possess the rightful permission!")
    print()

#----------------------------------------------------------------------------

# Define Show tables function               #function_working           #debugged
def show_tables():
    print()
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        myresult = cursor.fetchall()

        if myresult:
            for x in myresult:
                print(x)
            print()
        else:
            print("No tables found in the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print()

# Define create table function              #function_working           #debugged
def create_table():
    print()
    tablename = input("Enter table name: ")
    cols = int(input("Enter number of columns: "))
    colnames = []
    coltypes = []
    for i in range(cols):
        print()
        print("You are writing for column number: ", Fore.GREEN, i + 1 ,Style.RESET_ALL)
        colnames.append(input("Enter column name: "))
        coltypes.append(input("Enter column type along with dataconstraint: "))
        print()
    command = "CREATE TABLE " + tablename + "("
    for i in range(cols):
        command += colnames[i] + " " + coltypes[i]
        if i < cols - 1:  # not the last column
            command += ", "
    command += ")"
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Table created successfully.")
        #mydb.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        print()
    
#Describe table                             #function_working           #debugged
def describe_table():
   cursor = mydb.cursor()
   print()
   print("You have following tables available in your database: ")
   cursor.execute("SHOW TABLES")
   myresult = cursor.fetchall()
   print()
   for x in myresult:
       print(x)
   print()
   tablename=input("Enter the table name you want to describe: ")

   cursor = mydb.cursor()
   cursor.execute("DESCRIBE " + tablename)
   myresult = cursor.fetchall()

   for x in myresult:
      print(x)
   print()

# Define drop table function                #function_working           #debugged
def delete_from_table():
    print()
    show_tables()
    print()
    tablename = input("Enter table name: ")
    command = "DROP TABLE " + tablename
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Table dropped successfully.")
    except Exception as e:
        print(f"An erroccurred: {e}")
    print()

# Define delete table function              #function_working           #debugged
def drop_table():
    print()
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print()

    tablename = input("Enter table name: ")
    command = "TRUNCATE TABLE " + tablename

    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Content from Table deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()

#----------------------------------------------------------------------------

# Define the addcolumn()                    #function_working          #debugged
def addcolumn():
    print()
    print("You have following tables available in your database: ")
    print()
    show_tables()
    print()
    tablename = input("Enter table name : ")
    columnname = input("Enter column name : ")
    columntype = input("Enter column type ")
    columnval = input("Enter data constraint [Leave blank for no constraint] : ")
    command = f"ALTER TABLE {tablename} ADD {columnname} {columntype}({columnval});"

    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Column added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()

# Define the modifycolumn()                 #function_working          #debugged
def modifycolumn():
    print()
    print("You have following tables available in your database: ")
    print()
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print()
    print("Please select the table to view existing columns below: ")
    tablename = input("Enter table name : ")
    print()
    cursor.execute(f"DESCRIBE TABLE {tablename};")
    print()
    tablename = input("Enter table name : ")
    columnname = input("Enter column name : ")
    columntype = input("Enter column type ")
    columnval = input("Enter data constraint [Leave blank for no constraint] : ")
    command = f"ALTER TABLE {tablename} MODIFY {columnname} {columntype}({columnval});"

    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Column modified successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()

# Define the deletecolumn()                 #function_working           #check
def deletecolumn():
    print()
    print("Please select the table to view existing columns below: ")
    print()
    describe_table()
    print()
    tablename = input("Enter table name : ")
    columnname = input("Enter column name : ")
    command = f"ALTER TABLE {tablename} DROP COLUMN {columnname};"

    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Column deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print()


    times_input = int(input("How many entries do you want to insert into the table?: "))
    for i in range(times_input):
        print(f"Entry {i+1}:")
        cursor = mydb.cursor()
        print("You have following tables available in your database: ")
        print()
        show_tables()
        print()
        tablename = input("Enter the table name you want to insert data into: ")
        print()
        print("You have following columns available in your table: ")
        print()
        cursor.execute("DESCRIBE " + tablename)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        print()
        cols = int(input("Enter number of columns you want to insert data into: "))
        colnames = []
        colvalues = []
        for i in range(cols):
            colnames.append(input("Enter column name: "))
            colvalues.append(input("Enter column value: "))
        command = "INSERT INTO " + tablename + "("
        for i in range(cols):
            command += colnames[i]
            if i < cols - 1:
                command += ", "

#----------------------------------------------------------------------------

# Define Insert into table()                #function_working          #debugged
def insert_table():
    print()
    cursor = mydb.cursor()
    describe_table()
    print()
    print("Please enter the SQL Querries to enter insert data")
    query = input("Enter the SQL Querry: ")
    try:
        cursor = mydb.cursor()
        cursor.execute(query)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print()
     
# Define update function                    #function_error           #Debugged
def update_table():
  print()
  cursor = mydb.cursor()
  cursor.execute("SHOW TABLES")
  myresult = cursor.fetchall()
  for x in myresult:
    print(x)
  print()

  tablename = input("Enter the table name you want to update: ")
  print()

  cursor.execute("DESCRIBE " + tablename)
  print()
  command = input("Enter the SQL Query: ")
  try:
      cursor.execute(command)
      mydb.commit()
      print("Table updated successfully.")
  except Exception as e:
      print(f"An error occurred: {e}")
      mydb.rollback()
      print()

   
# Define delete function                    #function_error             #Debugged
def delete():
    print()
    print("You have the following tables available")
    show_tables()
    print()
    tablename = input("Enter the table name you want to delete data from: ")
    print()
    clause = input("Enter the clause: ")
    command = f"DELETE FROM {tablename} WHERE {clause};"
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        print("Data deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print()
    mydb.commit()
    print()
    print(cursor.rowcount, "record(s) deleted")
    print()

#----------------------------------------------------------------------------

# Define select function                    #function_working       #debugged
def select():
    cursor = mydb.cursor()
    print()
    cursor.execute("SHOW TABLES;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print()
    tablename = input("Enter table name: ")
    print()
    cursor.execute("DESCRIBE " + tablename)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    print()
    values = input("Enter columns to select: ")
    command = f"SELECT {values} FROM {tablename};"
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as e:
        print(f"An error occurred: {e}")
    print()

# Define select all function                #function_working               #debugged
def select_all():
    print()
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES;")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

    print()
    tablename = input("Enter table name: ")
    print()
    command = f"SELECT * FROM {tablename};"
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as e:
        print(f"An error occurred: {e}")
        print()

#----------------------------------------------------------------------------

# Define custom function                   #function_error              #Debugged
def custom():
    cursor = mydb.cursor()
    command = input("Enter the SQL Querry: ")
    try:
        cursor.execute(command)
        print("SQL Querry executed successfully.")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    except Exception as e:
        print(f"An error occurred: {e}")

#----------------------------------------------------------------------------

def csv():
    print()
    csvpath = "C:\\Users\\neela\\OneDrive\\Desktop\\flight_data.csv"
    cursor = mydb.cursor()
    
    try:
        print("Access denied!, you're using POPOAIRWAYS-IWQQ21 database")
        #cursor.execute("CREATE TABLE POPOAIRWAYS_DATA(SeatNo varchar(6) PRIMARY KEY NOT NULL,FirstName varchar(50),LastName varchar(50),Nationality char(15),Boarding_time varchar(20),Occupation char(20),inLuggage char(5),inFlight_Food char(5),Pet char(5))")
        with open(csvpath, "r") as csvfile:
            reader = csv.reader(csvfile)
             # Skip the header row (optional, adjust as needed)
            next(reader)
            for row in reader:
                sql = f"INSERT INTO POPOAIRWAYS_FLIGHTDATA (SeatNo, FirstName, LastName, Nationality, Boarding_time, Occupation, inLuggage, inFlight_Food, Pet) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}');"
                cursor.execute(sql)
            print("Flight data successfully imported from CSV!")
        mydb.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        print()
    

if __name__ == "__main__":
    connect_to_database()

try:
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")

        if user_input == 'exit':
            print("Goodbye!")
            break

        elif user_input in ['show tables','show table']:                                                   #show tables                     #function_working
            show_tables()
        
        elif user_input in ['create database','create databases','show database', 'show databases']:       #show databases                  #function_working
            print()
            show_database()
            print("You are using the database : " + Fore.GREEN + "POPOAIRWAYS-IWQQ21" + Style.RESET_ALL)
            print()
        
        elif user_input in ['delete database', 'delete databases']:                                        #show databases                  #function_working
           nopermission()
        
        elif user_input in ['create table','create tables']:                                               #creates table                   #function_working
           create_table()
        
        elif user_input in ['describe table','describe tables']:                                           #describes table                 #function_working
            describe_table()
        
        elif user_input in ['drop table','drop tables']:                                                   #deletes table                   #function_working
            drop_table()

        elif user_input in ['delete a table','delete from tables']:                                     #drops table                     #function_working
            delete_from_table()
        
        elif user_input in ['insert','insert in table']:                                                   #inserts data into table         #function_working
            insert_table()
        
        elif user_input in ['update','update table']:                                                     #updates data in table           #function_working
            update_table()
        
        elif user_input in ['add column','add columns']:                                                   #adds column to table            #function_working
            addcolumn()
        
        elif user_input in ['modify column','modify columns']:                                             #modifies column in table        #function_working
            modifycolumn()
        
        elif user_input in ['delete column','delete columns']:                                             #deletes column in table         #function_working
            deletecolumn()
        
        elif user_input in ['select']:                                                                      #selects data from table         #function_working
            select()
        
        elif user_input in ['select all','select*']:                                                        #selects all data from table     #function_working
            select_all()
        
        elif user_input in ['custom']:                                                                     #custom                          #function_tocheck
            custom()
        
        elif user_input in ['delete']:                                                                    #deletes data from table         #function_
            delete()
        
        elif user_input in ['csv']:
            csv()
        # Add elif statements for other commands and function
            
        #Error handlers
        elif user_input in ['Reconnect', 'reconnect']:
            reconnect_to_database()
        else:
            print("Command not recognized. Please use one of the provided commands.")

except KeyboardInterrupt:
    print("Operation aborted by the user.")
finally:
    # Close the database connection only when 'exit' is typed
    if mydb and mydb.is_connected():
        mydb.close()
        print("Connection to the database " + Fore.RED + "has been closed" + Style.RESET_ALL)
