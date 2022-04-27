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
@app.route("/home", methods = ['GET', 'POST'])
def Home():
    # get item from dynamodb table 'Users'
    userInfoJSON = request.json
    userInfo = dict(userInfoJSON)
    print("userInfo")
    print(userInfo)
    userID = userInfo.get("userId")
    print(userID)
    userTable = dynamodb.Table('Users')

    # get user from table and return json
    user = userTable.get_item(Key = {
        "UserID": str(userID)
    })
    print(user)
    return jsonify(user)

# this method is useless rn btw
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

    # still gets user for userProfile if user not logged in --> (scuffed way to do this. If someone has access to the code, they can log in to any user lmao)
    # could generate one every session here and send it
    userPassword = user.get("Item").get("Password")
    if(password == 'sgdfsd5897jds5hd3h3dfs56h4dhj56d4h756d545hftdh'):
        userPassword = 'sgdfsd5897jds5hd3h3dfs56h4dhj56d4h756d545hftdh'

    # returns info/user based on data entered
    if (len(user) == 2):                                                 # scuffed --> but works bc - if user, then theres two key entries in user dict
        if (userPassword == password):
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

    # checks for all fields filled in
    if(userInfoJSON.get("data").get("username") == '' or userInfoJSON.get("data").get("firstName") == '' or userInfoJSON.get("data").get("lastName") == '' or userInfoJSON.get("data").get("email") == ''):
        return jsonify("Invalid entry")

    userInfo = dict(userInfoJSON)

    if(userInfo.get("data").get("password") != userInfo.get("data").get("confirmPassword")):
        return jsonify("Invalid password")

    userTable = dynamodb.Table('Users')
    user = userTable.get_item(Key = {
        "UserID": userInfo.get("data").get("username")
    })
    print(user)

    if(len(user) != 2):
        userTable.put_item(
            Item = {
                "UserID": userInfo.get("data").get("username"),
                "Password": userInfo.get("data").get("password"),
                "lastName": userInfo.get("data").get("lastName"),
                "isAdmin": False,
                "reviews": [],
                "email": userInfo.get("data").get("email"),
                "firstName": userInfo.get("data").get("firstName"),
                "dateCreated": userInfo.get("data").get("dateCreated"),
                "isVerified": False
            }
        )
    else:
        return jsonify("Username already taken")

    # put some check here, but for now it works

    id = userInfo.get("data").get("username")
    user = userTable.get_item(Key = {
        "UserID": id
    })

    return jsonify(user)


@app.route("/post", methods = ['GET', 'POST'])
def Post():
    reviewInfoJSON = request.json
    reviewInfo = dict(reviewInfoJSON)
    reviewInfo = reviewInfo.get("review")
    userID = reviewInfo[1]
    reviewInfo = reviewInfo[0]

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

    return jsonify(response)

@app.route("/edit", methods = ['GET', 'POST'])
def Edit():
    reviewInfoJSON = request.json
    reviewInfo = dict(reviewInfoJSON)
    reviewInfo = reviewInfo.get("data")
    userID = reviewInfo[1]
    reviewInfo = reviewInfo[0]

    # get dynamodb table 'Users', put review into user
    userTable = dynamodb.Table('Users')                     # will eventually probably have to be more efficient, only get user from table. Unless it only gets a dynamo reference
    user = userTable.get_item(Key = {
        "UserID": userID
    })

    newReviewInfo = user.get("Item").get("reviews")
    reviewID = reviewInfo.get("id")

    # gets review with correct id to replace
    reviewID = int(reviewID)
    deleteReviewNum = 0
    for i in range(0,len(newReviewInfo)):
        if reviewID == newReviewInfo[i].get("id"):
            deleteReviewNum = i
    newReviewInfo = list(newReviewInfo)
    del newReviewInfo[deleteReviewNum]
    newReviewInfo.append(reviewInfo)


    # replace review, put into db
    response = userTable.update_item(
        Key = {
            "UserID": userID
        },
        UpdateExpression = "set reviews=:r",
        ExpressionAttributeValues = {
            ':r': newReviewInfo
        }
    )

    # get updated user -> scuffed efficiency, maybe response returns the new user somewhere in there
    userTable = dynamodb.Table('Users')                     # will eventually probably have to be more efficient
    user = userTable.get_item(Key = {
        "UserID": userID
    })

    return jsonify(user)

@app.route("/browse")
def Browse():
    userTable = dynamodb.Table('Users')
    response = userTable.scan()
    return jsonify(response)

@app.route("/delete", methods = ['GET', 'POST'])
def Delete():
    reviewInfoJSON = request.json
    reviewInfo = dict(reviewInfoJSON)

    reviewInfo = reviewInfo.get("data")
    reviewInfo = list(reviewInfo)

    userID = reviewInfo[1]

    # gets review number
    reviewNum = reviewInfo[0]
    reviewNum = reviewNum[0]
    reviewNum = int(reviewNum)


    # get dynamodb table 'Users', put review into user
    userTable = dynamodb.Table('Users')                     # will eventually probably have to be more efficient, only get user from table. Unless it only gets a dynamo reference
    user = userTable.get_item(Key = {
        "UserID": userID
    })

    newReviewInfo = user.get("Item").get("reviews")
    for i in range(0, len(newReviewInfo)):

        if newReviewInfo[i].get("id") == reviewNum:
            del newReviewInfo[i]
            break

    response = userTable.update_item(
        Key = {
            "UserID": userID
        },
        UpdateExpression = "set reviews=:r",
        ExpressionAttributeValues = {
            ':r': newReviewInfo
        }
    )
    print(response)

    # return updated user
    user = userTable.get_item(Key = {
        "UserID": userID
    })
    return jsonify(user)

@app.route("/admin")
def adminPage():
    return None
    

if __name__ == '__main__':  # true only if run directly (not through flask run, from what I can tell)
    app.run(host='0.0.0.0', port=5000)