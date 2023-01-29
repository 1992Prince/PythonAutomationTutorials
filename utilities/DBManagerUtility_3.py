import configparser

import mysql.connector

def createDbConnection():
    global mydb
    mydb = mysql.connector.connect(
        #host=getConfig()['SQL']['host'], database='APIDevelop', user='root', password='root'
        host='localhost', database='APIDevelop',user='root',password='root'
     )

def getMySqlQuery(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchone()
    #print(myresult[0],"---",myresult)
    return myresult


