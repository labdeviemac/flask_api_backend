from flask import jsonify
from flask_restful import Resource, abort, reqparse
from services.Users import Users
import datetime
import ast


class UsersRoutesListAll(Resource):

    def get(self):
        try:
            users = Users()
            resultset = users.select()
            return jsonify(dict(ast.literal_eval(resultset)))
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class UsersRoutesListById(Resource):

    def get(self, id):
        try:
            users = Users()
            resultset = users.select_by_id(id)
            results = ast.literal_eval(resultset)

            if results:
                return jsonify(dict(results))
            else:
                return {
                           "acknowledge": False,
                           "content": "User not found"
                       }, 404
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class UsersRoutesInsert(Resource):

    def post(self):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=True)
            parameter.add_argument('surname', type=str, required=True)
            parameter.add_argument('age', type=int, required=True)
            parameter.add_argument('birthdate', type=str, required=True)
            parameter.add_argument('state', type=int, required=True)

            args = parameter.parse_args()
            current_date = datetime.datetime.now()
            data = (args["name"], args["surname"], args["age"], args["birthdate"], current_date, args["state"])

            users = Users()
            users.insert(data)

            return {
                       "acknowledge": True,
                       "return": "Successfully saved!"
                   }, 201

        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class UsersRoutesUpdate(Resource):

    def put(self, id):
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
            users.update(values, id)

            return {
                       "acknowledge": True,
                       "return": "Successfully updated!"
                   }, 200
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class UsersRoutesUpdatePatch(Resource):

    def patch(self, id):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=False)
            parameter.add_argument('surname', type=str, required=False)
            parameter.add_argument('age', type=int, required=False)
            parameter.add_argument('birthdate', type=str, required=False)

            args = parameter.parse_args()
            arguments = dict(args)
            values = {k: v for k, v in arguments.items() if v is not None}

            database_string = ''
            for k, v in values.items():
                database_string += f"{k} = '{v}', "

            users = Users()
            users.update(database_string.rstrip(", "), id)

            return {
                       "acknowledge": True,
                       "return": "Successfully updated!"
                   }, 200

        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class UsersRoutesDelete(Resource):

    def delete(self, id):
        try:
            users = Users()
            users.delete(id)
            return {}, 204
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})
