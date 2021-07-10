#https://docs.microsoft.com/en-us/azure/mysql/connect-python  => This way was not used in the code

import pyodbc
import pandas as pd
server='chess-wiz.database.windows.net'
database='pgnDB'
username='adminchesswizz'
password='Admin@12345'
driver='{SQL Server}'

#Remember to allow ur local IP in DB server firewall settings

# Construct connection string
try:
   conn =  pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
   print("Connection established")
except Exception as e:
  print("Error in connection")
  print(e)

#https://www.dataquest.io/blog/sql-insert-tutorial/

cursor = conn.cursor()

sql_show = "SELECT * FROM contacts"

sql_create = "CREATE TABLE contacts (" + \
 	"contact_id INT PRIMARY KEY);"

#print(sql_create)

cursor.execute(sql_create)


