import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "learningdb"
)

if not mydb.is_connected():
    print("❌ Failed to connect to the MySQL server.")
else:
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("✅ Database 'alx_book_store' created successfully!")

    mycursor.close()
    mydb.close()

    print("Database connection closed.")