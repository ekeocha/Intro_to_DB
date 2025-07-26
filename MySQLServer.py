import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "learningdb"
)

except mysql.connector.Error as e:
    print(f"❌ Error connecting to the MySQL server: {e}")
   

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("✅ Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()

print("Database connection closed.")