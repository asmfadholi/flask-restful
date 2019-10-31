from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get (self):
        return { 'About': 'Hello Worldes' }

api.add_resource(HelloWorld, '/')

if __name__ == '__name__':
    app.run(thraeded=True, port=5000)