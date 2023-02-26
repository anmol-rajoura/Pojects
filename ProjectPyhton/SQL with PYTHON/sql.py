import mysql.connector
from mysql.connector import Error
import pandas as pd
def create_server_connection(hot_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host = hot_name, user= user_name, passwd= user_password)
        print("My sql database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# put our MYSQL Terminal password
pw = "Anmol@1245"


# Database name
db = "mysql_python"
connection = create_server_connection("localhost", "root", pw)


# Create mysql_python

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database create successful")
    except Error as err:
        print(f"Error: '{err}'")
create_database_query = "Create database mysql_python"
create_database(connection, create_database_query)


# Connect to Database

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd= user_password,
            database = db_name)
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# Execute sql queries

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful")
    except Error as err:
        print(f"Error: '{err}'")