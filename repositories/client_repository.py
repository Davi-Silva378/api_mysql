from config import get_connection
import _mysql_connector

class ClientRepository:

    @staticmethod
    def create_client(name, email, phone):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO clientes (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, phone))
            connection.commit()
        except _mysql_connector.Error as err:
            print(f'Error inserting client: {err}')
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_clients():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clientes")
            clients = cursor.fetchall()
            return clients
        except _mysql_connector.Error as err:
            print(f'Error getting clients: {err}')
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def get_client_id(client_id):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM clientes WHERE id = %s", (client_id,))
            client = cursor.fetchone()
            return client
        except _mysql_connector.Error as err:
            print(f'Error getting client id: {err}')
        finally:
            cursor.close()
            connection.close()
    
    @staticmethod
    def update_client(client_id, name, email, phone):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = "UPDATE clientes SET name = %s, email = %s, phone = %s WHERE id = %s"
            cursor.execute(query, (name, email, phone, client_id))
            connection.commit()
        except _mysql_connector.Error as err:
            print(f'Error updating client: {err}')
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_clients(client_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = %s", (client_id,))
            connection.commit()
        except _mysql_connector.Error as err:
            print(f'Error deleting client: {err}')
        finally:
            cursor.close()
            connection.close()