import mysql.connector


class Connection:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="q1w2e3r4",
            database="flask_sample"
        )
