import configparser

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config

connect_Config = {
    'host' : getConfig()['SQL']['host'],
    'database' : getConfig()['SQL']['database'],
    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password']
    }




def getConnection():
    try:
        conn = mysql.connector.connect(host=getConfig()['SQL']['host'],database='APIDevelop',user='root',password='root')
        if conn.is_connected():
            print("Connection Successful")
            return conn
    except Error as e:
        print(e)