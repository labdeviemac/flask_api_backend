from flask import jsonify
import json
from flask.helpers import make_response
import mysql.connector
class Users():

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="q1w2e3r4",
            database="flask_sample"
        )

    def insert(self, values):
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO users VALUES (null, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.connection.commit()
            return cursor.rowcount
        except:
            raise Exception("Error")

    def select(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            data = dict()
            for x in result:
                data.update({ x[0]: { "name": x[1], "surname": x[2], "age": x[3], "birthdate": str(x[4]), "created_at": str(x[5]), "users_id": x[6]}})
            return json.dumps(data)
        except:
            raise Exception("Error")