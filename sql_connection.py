import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  #print("Opening mysql connection") #print function to check the mysql connection is running
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='test', database='onlinestore')

  return __cnx