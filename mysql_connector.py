import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="hosxp"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ovst")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)