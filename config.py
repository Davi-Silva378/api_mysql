import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        port=os.getenv('DB_PORT', '3306'),
        host=os.getenv('DB_HOST', 'mysql03-farm36.kinghost.net'),
        user=os.getenv('DB_USER', 'sistemaconsupl'),
        password=os.getenv('DB_PASSWORD', 'GRkDjvyZv22dfKh'),
        database=os.getenv('DB_DATABASE', 'sistemaconsupl')
    )