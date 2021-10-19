from flask import Flask
from flask_restful import Api
from services.usersRoutes import *

app = Flask(__name__)
api = Api(app)

# Routes for application
api.add_resource(UsersRoutesListAll, "/users")
api.add_resource(UsersRoutesInsert, "/users/new")
api.add_resource(UsersRoutesList, "/users/<string:name>")
api.add_resource(UsersRoutesUpdate, "/users/update")

if __name__ == "__main__":
    app.run(debug=True, port=7700)