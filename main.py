from flask import Flask
from flask_restx import Api, Resource, fields
from flask import request

def configure_routes(flask_app):
    app = Api(app = flask_app,
		  version = "1.0",
		  title = "F1 Driver Recorder",
		  description = "Manage info on all the pilots in the grid")

    driver_space = app.namespace('driver', description='Manage drivers')

    driver_model = app.model('Driver Model',
                    {'name': fields.String(required = True, description="Name of the person", help="Name cannot be blank."),
                    'short_name': fields.String(required = True, description="Three letter id of the person", help="Short name cannot be blank."),
                    'car_number': fields.Integer(required = True, description="Car number acording to FIA specification", help="Car number cannot be blank."),
                    'constructor': fields.String(required = True, description="Constructor of the car", help="Constructor cannot be blank.")
                    })

    driver_list = {}

    @driver_space.route("/<int:id>")
    class MainClass(Resource):

        @app.doc(responses={
                    200: 'OK',
                    400: 'Invalid Argument',
                    500: 'Mapping Key Error'
                    },
                params={ 'id': 'Specify the Id associated with the driver' })

        def get(self, id):
            try:
                driver = driver_list[id]
                return {
                    "status": "Driver info retrieved",
                    "name" : driver["name"],
                    "short_name" : driver["short_name"],
                    "car_number" : driver["car_number"],
                    "constructor" : driver["constructor"]
                }
            except KeyError as e:
                driver_space.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
            except Exception as e:
                driver_space.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")

        @app.doc(responses={
                    200: 'OK',
                    400: 'Invalid Argument',
                    500: 'Mapping Key Error'
                    },
                params={ 'id': 'Specify the Id associated with the driver' })
        
        @app.expect(driver_model)

        def post(self, id):
            try:
                driver_list[id] = {
                    "name" : request.json["name"],
                    "short_name" : request.json["short_name"],
                    "car_number" : request.json["car_number"],
                    "constructor" : request.json["constructor"]
                }
                return {
                    "status": "New driver added",
                    "name" : driver_list[id]["name"],
                    "short_name" : driver_list[id]["short_name"],
                    "car_number" : driver_list[id]["car_number"],
                    "constructor" : driver_list[id]["constructor"]
                }
            except KeyError as e:
                driver_space.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
            except Exception as e:
                driver_space.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

app = Flask(__name__)

driver_list = {}

configure_routes(app)

if __name__ == '__main__':
    app.run()