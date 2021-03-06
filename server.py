# webframe work
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
# database
from sqlalchemy import create_engine
import pymysql
# data manipulation
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
myconnection = create_engine('mysql+pymysql://angelo:!Qry778899@127.0.0.1/angelo?charset=utf8')

app = Flask(__name__)
cors = CORS(app, resorces={r'/d/*': {"origins": '*'}})
api = Api(app)
CORS(app, origins="http://127.0.0.1:5002/", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)

# dummy data tables
class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'Trackdata': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

# spotify database tables    
class MyMusic(Resource):
    def get(self):
        conn = myconnection.connect()
        # get different attributes for each song
        query = conn.execute("select valence, song_name, loudness, energy from mymusic;")
        result = {'musicdata': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(MyMusic,'/mymusic') # Route_4

# following line will not run on pythonanywhere
if __name__ == '__main__':
     app.run(port='5002')