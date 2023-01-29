import mysql.connector

from utilities.sqlutilityconfig import *

"""
host, database, usernmae, password
conn = mysql.connector.connect(host='localhost',database='APIDevelop',
                       # user='root',password='root')
                       """

conn = getConnection()
print("Checking connection :",conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
#row = cursor.fetchone()
#print("First row data is :",row) # it will print data in tuple format
#print(row[3]," ",row[0])

allrows = cursor.fetchall()
print(allrows) # allrows will be list of tuples
sum = 0
for row in allrows:
    sum = sum + row[2]

print("Summation amount is :",sum)

conn.close()

# [] represets list
# () represents tuple






