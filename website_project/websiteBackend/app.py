from asyncio.windows_events import NULL
import os, json, boto3, requests        # look up what requests does exactly
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from boto3.dynamodb.conditions import Key, Attr

# Run flask app and cors =  browser compatibility basically
app = Flask(__name__)  #  name == special name for module
cors = CORS(app)

# set dynamo variable
dynamodb = boto3.resource("dynamodb")

app.url_map.strict_slashes = False
SECRET_KEY = os.environ.get('SECRET_KEY')


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
        return jsonify("Invalid entry")

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

@app.route("/register", methods = ['GET', 'POST'])
def Register():
    # get username from data sent
    userInfoJSON = request.json
    if(userInfoJSON.get("data").get("username") == ''):
        return jsonify("Invalid entry")

    userInfo = dict(userInfoJSON)

    if(userInfo.get("data").get("password") != userInfo.get("data").get("confirmPassword")):
        return jsonify("Invalid password")


    userTable = dynamodb.Table('Users')
    userTable.put_item(
        Item = {
            "UserID": userInfo.get("data").get("username"),
            "Password": userInfo.get("data").get("password"),
            "lastName": userInfo.get("data").get("lastName"),
            "isAdmin": False,
            "reviews": [],
            "email": userInfo.get("data").get("email"),
            "firstName": userInfo.get("data").get("firstName"),
            "isVerified": False
        }
    )



    # put some check here, but for now it works

    id = userInfo.get("data").get("username")
    user = userTable.get_item(Key = {
        "UserID": id
    })

    return jsonify(user)
    #if jsonify(userCheck) == jsonify(userInfo):
    #    return jsonify(userCheck)
    #else:
    #    return "Failure"


@app.route("/post", methods = ['GET', 'POST'])
def post():
    reviewInfoJSON = request.json
    reviewInfo = dict(reviewInfoJSON)
    reviewInfo = reviewInfo.get("review")
    userID = reviewInfo[1]
    reviewInfo = reviewInfo[0]

    #if(userInfoJSON.get("data").get("username") == ''):            --> Might not need bc other code checks this, modularity always good tho
    #    return jsonify("Invalid Entry")

    # get dynamodb table 'Users', put review into user
    userTable = dynamodb.Table('Users')                     # will eventually probably have to be more efficient, only get user from table. Unless it only gets a dynamo reference
    user = userTable.get_item(Key = {
        "UserID": userID
    })

    newReviewInfo = user.get("Item").get("reviews")
    newReviewInfo = list(newReviewInfo)
    newReviewInfo.append(reviewInfo)
    response = userTable.update_item(
        Key = {
            "UserID": userID
        },
        UpdateExpression = "set reviews=:r",
        ExpressionAttributeValues = {
            ':r': newReviewInfo
        }
    )

    return response



@app.route("/browse")
def Browse():
    userTable = dynamodb.Table('Users')
    #userDataList = userTable.query(
        #KeyConditionExpression=Key('UserID')
    #)
    #userTable = dict(userTable)
    response = userTable.scan()

    # get user from table and return json
    #userList = []
    #userId = 1
    #for i in range(0,5):
        #user = userTable.get_item(Key = {
            #"UserID": str(userId)
        #})
        #userList.append(user)
        #userId += 1
        #print("User number")
        #print(userId)
        #print(user)
    #print('right here!!')
    #print(userList)
    #return jsonify(userList)

    return jsonify(response)

@app.route("/admin")
def adminPage():
    return NULL
    

if __name__ == '__main__':  # true only if run directly (not through flask run, from what I can tell)
    app.run(debug=True)