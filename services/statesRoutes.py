from flask_restful import Resource, abort, reqparse
from services.States import States
import ast


class StatesRoutesListAll(Resource):

    def get(self):
        try:
            states = States()
            resultset = states.select()
            return {
                "acknowledge": True,
                "content": ast.literal_eval(resultset)
            }, 200
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class StatesRoutesListById(Resource):

    def get(self, id):
        try:
            states = States()
            resultset = states.select_by_id(id)
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
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class StatesRoutesInsert(Resource):

    def post(self):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('statename', type=str, required=True)
            parameter.add_argument('statecode', type=str, required=True)

            args = parameter.parse_args()
            data = (args["statename"], args["statecode"])

            states = States()
            states.insert(data)
            return {
                "acknowledge": True,
                "return": "Successfully saved!"
            }, 201
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class StatesRoutesUpdate(Resource):

    def put(self, id):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('statename', type=str, required=True)
            parameter.add_argument('statecode', type=str, required=True)

            args = parameter.parse_args()
            values = f"state_name = {args['statename']}, state_shorname = {args['statecode']}"

            states = States()
            states.update(values, id)

            return {
                "acknowledge": True,
                "return": "Successfully updated!"
            }, 200
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class StatesRoutesUpdatePatch(Resource):

    def patch(self, id):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('statename', type=str, required=False)
            parameter.add_argument('statecode', type=str, required=False)

            args = parameter.parse_args()
            arguments = dict(args)
            values = {k: v for k, v in arguments.items() if v is not None}

            database_string = ''
            for k, v in values.items():
                database_string += f"{k} = '{v}', "

            states = States()
            states.update(database_string.rstrip(", "), id)

            return {
                "acknowledge": True,
                "return": "Successfully updated!"
            }, 200

        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})


class StatesRoutesDelete(Resource):

    def delete(self, id):
        try:
            states = States()
            states.delete(id)
            return {}, 204
        except:
            return abort(400, message={"acknowledge": False, "reason": "Error while executing request!"})