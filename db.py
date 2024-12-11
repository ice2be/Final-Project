import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="####",
        port="####",
        user="####",
        password="####",
        database="####"
    )
    return db
