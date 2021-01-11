
from flask import Flask, abort
from flask_restful import Resource, Api
from random import choices

app = Flask(__name__)
api = Api(app)

class Default(Resource):
    def get(self):
        return {}, choices([200, 404, 500], weights = [5, 1, 1], k = 1)[0]

api.add_resource(Default, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
