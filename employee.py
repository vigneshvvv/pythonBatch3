from db import DataBase

class fetchBooks:
    def fetchAllData(self):
        conn = DataBase.get_connection()
        cursor = conn.cursor()

        cursor.execute("select * from books")

        data = cursor.fetchall()

        cursor.close()
        conn.close()
        return data
    


emp = fetchBooks()
print(emp.fetchAllData())    