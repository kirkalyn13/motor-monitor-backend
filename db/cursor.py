import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_port = os.environ.get("DB_PORT")

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password,
    port=db_port,
)

def query(query_string):
    try:
        cursor = connection.cursor()
        cursor.execute(query_string)
        connection.commit()
        return cursor.fetchall()
    except Exception as e:
        print(f"Executed: {query_string}")
        print(f"Error Occurred: {e}")
    finally:
        cursor.close()



