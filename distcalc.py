from flask import Flask
from flask_restful import Api, Resource, reqparse

distcalc = Flask(__name__)
api = Api(distcalc)

circles = [
	{
		"id": 1,
		"radius": 2
	},
	{
		"id": 2,
		"radius": 4
	}
]

class distance(Resource):
	def get(self, radius):
		for circle in circles:
			if(radius == circle["radius"]):
				return circle, 200
		return "Circle not found", 404
	
	def post(self, radius):
		parser = reqparse.RequestParser()
		parser.add_argument("id")
		args = parser.parse_args()
		
		for circle in circles:
			if(radius == circle["radius"]):
				return "exists", 400
		circle = {
			"id": args["id"],
			"radius": radius
		}
		
		circles.append(circle)
		return circle, 201

api.add_resource(distance, "/circle/<int:radius>")

distcalc.run(debug=True)
