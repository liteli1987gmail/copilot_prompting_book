import sqlite3
import flask

# Expose a REST API endpoint using the Flask framework \
# to serve a JSON-serialized list of books queried from \
# a file-based SQLite database.

app = flask.Flask(__name__)

@app.route("/books")
def get_books():
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return flask.jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)