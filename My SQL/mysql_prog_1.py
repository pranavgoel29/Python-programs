import mysql.connector
import os

os.system("cls")

db = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "root",
    database = "testdatabase"
    )
 
mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Person (name varchar(30), age int, personID int PRIMARY KEY AUTO_INCREMENT)")

# mycursor.execute("DESCRIBE Person")

# mycursor.execute("INSERT INTO Person (name, age) VALUES ('Pranav', 19)")
# db.commit()

mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)

