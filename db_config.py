import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Change if necessary
        password="root",  # Change if necessary
        database="assignment3_db"
    )