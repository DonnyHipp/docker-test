import pyodbc
server = 'tcp:sqlprd_prd_pmru_lms.dbaas.sdi.pmi\PRD'
database = 'prd_pmru_lms'
username = 'S-SDI-PMRU-RW-APP-SQL'
password ='Y7q###26#9t8+TT'
connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
print(connection_string)
cnxn = pyodbc.connect(connection_string)
cursor = cnxn.cursor()
cursor.execute("SELECT [id],[value] FROM [prd_pmru_lms].[dbo].[TestTable]")
result= cursor.fetchall()
print(result)
cnxn.close()