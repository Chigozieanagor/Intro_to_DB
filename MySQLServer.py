import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Bestway@71always",
    
    )
    print("Database is open")
    mycursor = mydb.cursor()


    mycursor.execute(
    "CREATE DATABASE IF NOT EXISTS alx_book_store"
    )
    mycursor.close()
    mydb.close()

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Bestway@71always",
        database = "alx_book_store"
    )
    print("Database 'alx_book_store' created successfully!")
    
except Error as e:
    print(f"Error: {e}")
finally:
    try:
        if mycursor:
            mycursor.close()
    except:
        pass
    try:
        if mydb.is_connected():
            mydb.close()
    except:
        pass

print("\nDatabase is closed")