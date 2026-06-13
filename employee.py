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
    
    def insertBooks(self, id, bookName, author, price):
        conn = DataBase.get_connection()
        cursor = conn.cursor()

        query = """INSERT INTO books values (%s, %s, %s, %s)"""

        values = (id, bookName, author, price)
        cursor.execute(query, values)
        conn.commit()
        print("inserted successfully")
        cursor.close()
        conn.close()
        return "inserted successfully"
    


# emp = fetchBooks()
# # print(emp.fetchAllData()) 
# emp.insertBooks(21, "Mein kampf", "AH", 1500)   
