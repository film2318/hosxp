
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="hosxp"
)

try:
    query = "SELECT * FROM patient"
    df = pd.read_sql(query, mydb)

    # แสดงข้อมูลเป็นตาราง
    print(df.to_string(index=False))

finally:
    mydb.close()
