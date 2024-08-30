import mysql.connector

class modeloproducto:
    def __init__(self):
        self.conn= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="inicio"
        )
        self.cursor=self.conn.cursor()
