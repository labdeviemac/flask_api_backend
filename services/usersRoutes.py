from flask_restful import Resource, abort, reqparse, request
import ast  # Biblioteca Abstract Syntax Trees
from .Users import Users
import datetime

class UsersRoutes(Resource):
    
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
            return { "acknowledge": True, "content": ast.literal_eval(resultset) }
        except:
            return abort(400, message={"message": "Error"})

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

            return { "acknowledge": True, "return": "Successfully saved!" }

        except:
            return abort(400, message={"message": "Error"})
    
class UsersRoutesList(Resource):

    def get(self, name):
        try:
            users = Users()
            resultset = users.select_by_name(name)
            results = ast.literal_eval(resultset)

            if results: 
                return { "acknowledge": True, "content": results }
            else:
                return { "acknowledge": False, "content": "Item not found" }
        except:
            return abort(400, message={"message": "Error"})