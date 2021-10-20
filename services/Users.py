import json
from services.Connection import Connection


class Users(Connection):

    def insert(self, values):
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO users VALUES (null, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e

    def select(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()
            data = dict()
            for x in result:
                data.update(
                    {
                        x[0]: {
                            "name": x[1],
                            "surname": x[2],
                            "age": x[3],
                            "birthdate": str(x[4]),
                            "created_at": str(x[5]),
                            "users_id": x[6]
                        }
                    }
                )
            return json.dumps(data)
        except Exception as e:
            return e

    def select_by_id(self, iduser):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM users u JOIN states s ON s.id = u.users_id WHERE u.id = {iduser}")
            result = cursor.fetchall()
            data = dict()
            for x in result:
                data.update(
                    {
                        "id": x[0],
                        "name": x[1],
                        "surname": x[2],
                        "age": x[3],
                        "birthdate": str(x[4]),
                        "created_at": str(x[5]),
                        "state_name": x[8],
                        "state_code": x[9]
                    }
                )
            return json.dumps(data)
        except Exception as e:
            return e

    def update(self, data, clause):
        cursor = self.connection.cursor()
        try:
            sql = f"UPDATE users SET {data} WHERE id = {clause}"
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e

    def delete(self, iduser):
        cursor = self.connection.cursor()
        try:
            sql = f"DELETE FROM users WHERE id = {iduser}"
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e
