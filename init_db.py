from config import get_connection
import mysql.connector

def create_tables():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        create_table_query = """
                CREATE TABLE IF NOT EXISTS clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL, 
                    email VARCHAR(255) NOT NULL,
                    phone VARCHAR(50) NOT NULL
                ) 
                """
        cursor.execute(create_table_query)
        connection.commit()
    except mysql.connector.Error as err:
        print(f'Error creating tables: {err}')
        connection.rollback()
    finally:
        cursor.close()
        connection.close()