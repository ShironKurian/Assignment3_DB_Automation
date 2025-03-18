from flask import Flask, render_template, request
from db_config import get_db_connection

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()

        return "User registered successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)