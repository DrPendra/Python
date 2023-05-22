import mysql.connector
from mysql.connector import Error


database='biblio'
'''
try:
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
'''
'''
try:
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user='root',
                                         password='')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

'''
'''
try:
    connection_config_dict = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': database,
        'raise_on_warnings': True,
        'use_pure': False,
        'autocommit': True,
        'pool_size': 5
    }
    connection = mysql.connector.connect(**connection_config_dict)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

'''
try:
    connection = mysql.connector.connect(host='localhost',
                                         database=database,
                                         user='root',
                                         password='', connection_timeout=180)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)

        cursor = connection.cursor()
        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)

        sql_select_Query = "select * from client"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        for row in records:
            print("ID = ", row[0], )
            print("Nom = ", row[1])
            print("Prenom  = ", row[2], "\n")
        cursor.close()

        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        for row in records:
            id = row["id"]
            nom = row["nom"]
            prenom = row["prenom"]

            print(f'Client, id :{id} nom : {nom} prénom : {prenom}')

        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
