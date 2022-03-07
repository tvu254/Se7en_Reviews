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
SECRET_KEY = os.environ.get('SECRET_KEY')
#app.secret_key = os.urandom(12).hex()
#app.config['SECRET_KEY'] = "Your_secret_string"


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

@app.route("/login", methods = ['GET', 'POST'])
def loginPage():
    # get username from data sent
    userInfoJSON = request.json
    if(userInfoJSON.get("data").get("username") == ''):
        return jsonify("Invalid Entry")

    userInfo = dict(userInfoJSON)
    userID = userInfo.get("data").get("username")
    password = userInfo.get("data").get("password")

    # get item from dynamodb table 'Users'
    userTable = dynamodb.Table('Users')

    # get user from table and return json if found
    user = userTable.get_item(Key = {
        "UserID": userID
    })

    # returns info/user based on data entered
    if (len(user) == 2):                                                 # scuffed --> but works bc - if user, then theres two key entries in user dict
        if (user.get("Item").get("Password") == password):
            return jsonify(user)
        else:
            return jsonify("Invalid Password")
    elif (len(user) == 1):
        return jsonify("Failed to find user")
    else:
        return jsonify("Something went horribly wrong")

@app.route("/post", methods = ['GET', 'POST'])
def post():
    print("hey")
    reviewInfoJSON = request.json
    reviewInfo = dict(reviewInfoJSON)
    print(reviewInfo)
    reviewInfo = reviewInfo.get("review")
    print(reviewInfo)
    userID = reviewInfo[1]
    print(userID)
    reviewInfo = reviewInfo[0]
    print(reviewInfo)

    #if(userInfoJSON.get("data").get("username") == ''):
    #    return jsonify("Invalid Entry")

    # get dynamodb table 'Users', put review into user
    userTable = dynamodb.Table('Users')                     # will eventually probably have to be more efficient, only get user from table
    user = userTable.get_item(Key = {
        "UserID": userID
    })
    print(user)

    # Might have to delete the user from dynamodb, insert the review, and add it back to dynamo

    #user.get("Item").get("Password")
    #userTable.update_item(
        #Key = {
            #"UserID": userID
        #},
        #UpdateExpression = "set reviews"
    #)

    return NULL

@app.route("/admin")
def adminPage():
    return NULL
    

if __name__ == '__main__':  # true only if run directly (not through flask run, from what I can tell)
    app.run(debug=True)