from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS     #comment this on deployment
from core.HelloApiHandler import HiApiHandler


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app) # comment this on dployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/auth/myhome")
def hello_you():
    return "hello "


@app.route('/auth/profile')
def my_profile():
    response_body = {

        "name": "Changl",
        "about": "I am full stack developer"
    }
    return response_body  




@app.route('/jcl/hi')
def hi_jcl():
    return 'hello jcl'


api.add_resource(HiApiHandler, '/auth/hi')



"""

CORS error message:
    Why does my JavaScript code receive a "No 'Access-Control-Allow-Origin' header is present on the requested resource" error, while Postman does not?l

"""
