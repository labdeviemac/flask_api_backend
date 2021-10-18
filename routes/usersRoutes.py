from flask_restful import Resource, abort, reqparse 
from services.States import States

class UsersRoutes(Resource):
    
    def get(self):
        try:
            states = States()
            retorno = states.teste("Not an error! Executed successfully")
            return {"acknowledge": True, "message": "Return successful", "return": retorno }
        except:
            return abort(400, message={"message": "Error"})

    def post(self):
        try:
            parameter = reqparse.RequestParser()
            parameter.add_argument('name', type=str, required=True)
            args = parameter.parse_args()

            return { "acknowledge": True, "return": args["name"] }
        except:
            return abort(400, message={"message": "Error"})
    
class UsersRoutesList(Resource):

    def get(self, nome):
        try:
            return { "acknowledge": True, "return": nome }
        except:
            return abort(400, message={"message": "Error"})