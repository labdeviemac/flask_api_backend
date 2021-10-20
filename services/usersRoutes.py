from flask_restful import Resource, abort, reqparse
from services.Users import Users
import datetime
import ast


class UsersRoutesListAll(Resource):

    def get(self):
        try:
            users = Users()
            resultset = users.select()
            """
            O comando literal_eval é um interessante comando da biblioteca 
            Python ast – Abstract Syntax Trees. Ele avalia uma string contendo 
            uma expressão Python e a executa.

            O literal_eval funciona de maneira semelhante ao conhecido comando 
            eval, porém aceita apenas um pequeno conjunto de estruturas Python: 
            strings, números, dicionários, listas, tupla, valores boleanos(True 
            ou False) ou None. A partir da versão 3.2, ele também passou a 
            aceitar bytes e set.
            """
            # Esta função transforma strings em um objeto Python
            return {
                       "acknowledge": True,
                       "content": ast.literal_eval(resultset)
                   }, 200
        except:
            return abort(400, message={"message": "Error"})


class UsersRoutesInsert(Resource):

    def post(self):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=True)
            parameter.add_argument('surname', type=str, required=True)
            parameter.add_argument('age', type=int, required=True)
            parameter.add_argument('birthdate', type=str, required=True)

            args = parameter.parse_args()
            current_date = datetime.datetime.now()
            data = (args["name"], args["surname"], args["age"], args["birthdate"], current_date, 1)

            users = Users()
            users.insert(data)

            return {
                       "acknowledge": True,
                       "return": "Successfully saved!"
                   }, 201

        except:
            return abort(400, message={"message": "Error"})


class UsersRoutesList(Resource):

    def get(self, iduser):
        try:
            users = Users()
            resultset = users.select_by_id(iduser)
            results = ast.literal_eval(resultset)

            if results:
                return {
                           "acknowledge": True,
                           "content": results
                       }, 200
            else:
                return {
                           "acknowledge": False,
                           "content": "User not found"
                       }, 404
        except:
            return abort(400, message={"message": "Error"})


class UsersRoutesUpdate(Resource):

    def put(self, iduser):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=True)
            parameter.add_argument('surname', type=str, required=True)
            parameter.add_argument('age', type=int, required=True)
            parameter.add_argument('birthdate', type=str, required=True)

            args = parameter.parse_args()
            values = f"name = '{args['name']}', surname = '{args['surname']}', age = {args['age']}, " \
                     f"birthdate = '{args['birthdate']}'"

            users = Users()
            users.update(values, iduser)

            return {
                       "acknowledge": True,
                       "return": "Successfully updated!"
                   }, 200
        except:
            return abort(400, message={"message": "Error"})


class UsersRoutesUpdatePatch(Resource):

    def patch(self, iduser):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=False)
            parameter.add_argument('surname', type=str, required=False)
            parameter.add_argument('age', type=int, required=False)
            parameter.add_argument('birthdate', type=str, required=False)

            args = parameter.parse_args()
            arguments = dict(args)
            values = {k: v for k, v in arguments.items() if v is not None and k != "id"}

            database_string = ''
            for k, v in values.items():
                database_string += f"{k} = '{v}', "

            users = Users()
            users.update(database_string.rstrip(", "), iduser)

            return {
                       "acknowledge": True,
                       "return": "Successfully updated!"
                   }, 200

        except:
            return abort(400, message={"message": "Error"})


class UsersRoutesDelete(Resource):

    def delete(self, iduser):
        try:
            users = Users()
            users.delete(iduser)
            return {}, 204
        except:
            return abort(400, message={"message": "Error"})
