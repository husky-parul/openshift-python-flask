from flask import Flask
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    # return "Hello World Parul!"
    return jsonify("Hello World Parul!")

@application.route("/cpu")
def lotsofcpu():
    # do a lot of cpu work
    arr = [0] * 20000000
    sum = 1
    for i in range(len(arr)):
        sum+=arr[i]
    
    data = "sum " + str(sum)
    return jsonify(data)
    


if __name__ == "__main__":
    application.run()