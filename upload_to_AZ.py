#https://docs.microsoft.com/en-us/azure/mysql/connect-python  => This way was not used in the code
#https://datatofish.com/create-table-sql-server-python/

import pyodbc
import pandas as pd
import csv
import sqlalchemy
from sqlalchemy import create_engine

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

sql_all_tables = "SELECT * FROM information_schema.tables"
all_tables = cursor.execute(sql_all_tables)

tables = []
for table in all_tables:
  tables.extend(list(table))

if("results_chess" not in  tables):
  
  sql_create =   '''
  CREATE TABLE results_chess (
    Event varchar(255),
    Site varchar(255),
    Date varchar(255),
    Round varchar(255),
    White varchar(255),
    Black varchar(255),
    Result varchar(255),
    WhiteElo varchar(255),
    BlackElo varchar(255),
    ECO varchar(255),
      )
  '''

  print(sql_create)

  cursor.execute(sql_create)
  conn.commit()

df1 = pd.read_csv("data/csv/Aachen1868.csv")

#https://docs.microsoft.com/en-us/sql/machine-learning/data-exploration/python-dataframe-sql-server?view=sql-server-ver15
#Insert Dataframe into SQL Server:
for index, row in df1.iterrows():
  print(index)
  cursor.execute("INSERT INTO results_chess (Event,	Site,	Date,	Round,	White, Black,	Result,	WhiteElo,	BlackElo,	ECO) values(?,?,?,?,?,?,?,?,?,?)", str(row.Event),	str(row.Site),	str(row.Date),	str(row.Round),	str(row.White),	str(row.Black),	str(row.Result),	str(row.WhiteElo),	str(row.BlackElo),	str(row.ECO))
conn.commit()


#https://stackoverflow.com/questions/59362559/using-python-to-import-csv-from-remote-machine-into-azure-sql-server
# with conn.cursor() as dw_curs:
#   with open("data/csv/Aachen1868.csv", 'r', encoding='utf-8') as csv_file:
#     next(csv_file, None)  # skip the header row
#     reader = csv.reader(csv_file, delimiter='|')
#     for row in csv_file:
#       dw_curs.execute('insert into results_chess (Event, Site, Date, Round, White, Black, Result, WhiteElo, BlackElo, ECO) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

# SQL_insert = '''BULK INSERT results
# FROM 'data/csv/Anand.csv'
# WITH ( FORMAT='CSV')'''



# from sqlalchemy import create_engine
# engine = sqlalchemy.create_engine(
#                "mssql+pyodbc://user:pwd@server/database",
#                echo=False)

# data.to_sql('test', con=engine, if_exists='replace')
# df1.to_sql("results_chess",conn, if_exists = "append")



#https://towardsdatascience.com/use-python-and-bulk-insert-to-quickly-load-data-from-csv-files-into-sql-server-tables-ba381670d376
# def insert_data(conn, csv_file_nm, db_table_nm):
#   # Insert the data from the CSV file into the database table.
#   # Assemble the BULK INSERT query. Be sure to skip the header row by specifying FIRSTROW = 2.
#   qry = "BULK INSERT " + db_table_nm + " FROM '" + csv_file_nm + "' WITH (FORMAT = 'CSV', FIRSTROW = 2)"
#   # Execute the query
#   cursor = conn.cursor()
#   success = cursor.execute(qry)
#   conn.commit()
#   cursor.close

# insert_data(conn,"data/csv/Aachen1868.csv","results_chess")

SQL_Query = pd.read_sql_query("SELECT * FROM results_chess", conn)
 
df = pd.DataFrame(SQL_Query)

print(df.head())

cursor.close()