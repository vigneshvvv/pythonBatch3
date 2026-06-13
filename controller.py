from flask import Flask, request
from employee import fetchBooks

app = Flask(__name__)

@app.route("/getBooks", methods=["GET"])
def get_book_details():
    obj = fetchBooks()
    data = obj.fetchAllData()
    return data

@app.route("/insertBooks", methods=["POST"])
def insert_book_details():
    data = request.json
    obj = fetchBooks()
    result = obj.insertBooks(data["id"], data["bookName"], data["author"], data["price"])
    return result    

if __name__ == "__main__":
    app.run(debug=True)