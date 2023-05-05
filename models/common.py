import psycopg2
import os

db_env_constant = "DATABASE_URL"

def sql_read(query, parameters=[]):
    connection = psycopg2.connect(os.getenv(db_env_constant))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.close()
    return results

def sql_write(query, parameters=[]):
    connection = psycopg2.connect(os.getenv(db_env_constant))
    cursor = connection.cursor()
    cursor.execute(query, parameters)
    connection.commit()
    connection.close()