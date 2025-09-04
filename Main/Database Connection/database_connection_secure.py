import mysql.connector

def check_mysql_connection():
    try:
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='test',
    )
    finally:
        print("Successfully connected to MySQL!")
        connection.close()
        
# Will be continued later... 