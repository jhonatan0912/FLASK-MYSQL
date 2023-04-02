from flask import Flask, request, jsonify
from mysql.connector import connect, Error

app = Flask(__name__)


def get_database_connection():
    try:
        connection = connect(
            host="localhost",
            user="root",
            password="1234",
            database="hotel_torre_torre"
        )
        print("Successfully connected to database")
        return connection
    except Exception as e:
        print("Error connecting to database")
        return None


@app.route('/rooms', methods=['GET'])
def get_rooms():
    # Get a database connection
    db_connection = get_database_connection()
    if db_connection is None:
        return jsonify({"error": "Could not connect to database"})
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM room")
    rooms = cursor.fetchall()
    cursor.close()

    return jsonify(rooms)


if __name__ == "__main__":
    app.run(debug=True)
