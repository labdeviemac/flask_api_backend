from services.Connection import Connection
import json


class States(Connection):

    def insert(self, data):
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO states VALUES (null, %s, %s)"
            cursor.execute(sql, data)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e

    def select(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM states")
            result = cursor.fetchall()
            data = dict()
            for x in result:
                data.update(
                    {
                        x[0]: {
                            "state": x[1],
                            "statecode": x[2]
                        }
                    }
                )
            return json.dumps(data)
        except Exception as e:
            return e

    def select_by_id(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM states WHERE u.id = {id}")
            result = cursor.fetchall()
            data = dict()
            for x in result:
                data.update(
                    {
                        "id": x[0],
                        "state": x[1],
                        "statecode": x[2]
                    }
                )
            return json.dumps(data)
        except Exception as e:
            return e

    def update(self, data, clause):
        cursor = self.connection.cursor()
        try:
            sql = f"UPDATE states SET {data} WHERE id = {clause}"
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e

    def delete(self, id):
        cursor = self.connection.cursor()
        try:
            sql = f"DELETE FROM states WHERE id = {id}"
            cursor.execute(sql)
            self.connection.commit()
            return cursor.rowcount
        except Exception as e:
            return e
