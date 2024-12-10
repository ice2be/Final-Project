import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host="ice2be.com",
        port="40355",
        user="root",
        password="oddball55",
        database="florida_international_university"
    )
    return db
