import mysql.connector

class DataBase:
    def get_connection():
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database= "javatrainingpro"
        )

        return conn
