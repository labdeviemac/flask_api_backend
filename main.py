from flask import Flask
from flask_restful import Api
from services.usersRoutes import *

app = Flask(__name__)
api = Api(app)

# Routes for application
api.add_resource(UsersRoutesListAll, "/users")  # GET
api.add_resource(UsersRoutesInsert, "/users")  # POST
api.add_resource(UsersRoutesList, "/users/<int:iduser>")  # GET
api.add_resource(UsersRoutesUpdate, "/users/<int:iduser>")  # PUT
api.add_resource(UsersRoutesUpdatePatch, "/users/<int:iduser>")  # PATCH
api.add_resource(UsersRoutesDelete, "/users/<int:iduser>")  # DELETE

if __name__ == "__main__":
    app.run(debug=True, port=7700)