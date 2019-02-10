#!/usr/bin/env python

#DB config settings
host = 'localhost'
database = 'rdmdb'
user = 'AccountWithPermissiontoModifytheDB'
password = 'YourStrongPassword'
port = '3306'

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   conn = mysql.connector.connect(host=host,
                             database=database,
                             user=user,
                             password=password,
                             port=port)
   cursor = conn.cursor()

   #Delete record now
   sql_Delete_query = """DELETE FROM pokemon WHERE expire_timestamp < UNIX_TIMESTAMP(DATE_SUB(NOW(), INTERVAL 12 HOUR));"""
   cursor.execute(sql_Delete_query)
   conn.commit()
   print (" ")
   print ("Pokemon Deleted successfully ")


except mysql.connector.Error as error :
    print("Failed to delete record to database: {}".format(error))

finally:
    #closing database connection.
    if(conn.is_connected()):
        conn.close()
        print("MySQL connection is closed")
