from flask import Flask
from flask_restful import Api
from routes.usersRoutes import *

app = Flask(__name__)
api = Api(app)

api.add_resource(UsersRoutes, "/users")
api.add_resource(UsersRoutesList, "/users/<string:nome>")

if __name__ == "__main__":
    app.run(debug=True, port=7700)