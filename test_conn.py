import pyodbc
import pandas as pd
server='chess-wiz.database.windows.net'
database='pgnDB'
username='adminchesswizz'
password='Admin@12345'   
driver='{SQL Server}'

conn =  pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
