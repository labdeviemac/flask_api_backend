from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from services.usersRoutes import *
from services.statesRoutes import *

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

# Routes for Users in Application
api.add_resource(UsersRoutesListAll, "/users")  # GET
api.add_resource(UsersRoutesInsert, "/users")  # POST
api.add_resource(UsersRoutesListById, "/users/<int:id>")  # GET
api.add_resource(UsersRoutesUpdate, "/users/<int:id>")  # PUT
api.add_resource(UsersRoutesUpdatePatch, "/users/<int:id>")  # PATCH
api.add_resource(UsersRoutesDelete, "/users/<int:id>")  # DELETE

# Routes for States in Application
api.add_resource(StatesRoutesListAll, "/states")  # GET
api.add_resource(StatesRoutesInsert, "/states")  # POST
api.add_resource(StatesRoutesListById, "/states/<int:id>")  # GET
api.add_resource(StatesRoutesUpdate, "/states/<int:id>")  # PUT
api.add_resource(StatesRoutesUpdatePatch, "/states/<int:id>")  # PATCH
api.add_resource(StatesRoutesDelete, "/states/<int:id>")  # DELETE


if __name__ == "__main__":
    app.run(debug=True, port=7700)
