from asyncio.windows_events import NULL
import os, json, boto3, requests        # look up what requests is for
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# Run flask app and cors =  browser compatibility basically
app = Flask(__name__)  #  name == special name for module
cors = CORS(app)

# set dynamo variable
dynamodb = boto3.resource("dynamodb")

app.url_map.strict_slashes = False
#SECRET_KEY = os.environ.get('SECRET_KEY')

# routes
@app.route("/")
@app.route("/home")
def Home():
    return NULL

@app.route("/user/<userId>", methods = ['GET']) # GET is the default method and not required
def userPage(userId):
    # get item from dynamodb table 'Users'
    userTable = dynamodb.Table('Users')

    # get user from table and return json
    user = userTable.get_item(Key = {
        "UserID": str(userId)
    })
    return jsonify(user)

@app.route("/admin")
def adminPage():
    return NULL
    

if __name__ == '__main__':  # true only if run directly (not through flask run, from what I can tell)
    app.run(debug=True)