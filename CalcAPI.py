
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message':'this is your calculator api'})

class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})

class Cube(Resource):
    def get(self, num):
        return jsonify({'cube': num**3})

class Sum(Resource):
    def get(self, num1, num2):
        return jsonify({'sum': num1 + num2})

class Difference(Resource):
    def get(self, num1, num2):
        return jsonify({'difference': num1 - num2})

class Product(Resource):
    def get(self, num1, num2):
        return jsonify({'product': num1*num2})

class Division(Resource):
    def get(self, num1, num2):
        return jsonify({'division': num1/num2})



api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Cube, '/cube/<int:num>')
api.add_resource(Sum, '/sum/<int:num1>/<int:num2>')
api.add_resource(Difference, '/difference/<int:num1>/<int:num2>')
api.add_resource(Product, '/product/<int:num1>/<int:num2>')
api.add_resource(Division, '/division/<int:num1>/<int:num2>')



if __name__ == '__main__':
    app.run(debug = True)
