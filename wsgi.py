from flask import Flask
from flask import jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    # return "Hello World Parul!"
    return jsonify("Hello World Parul!")

if __name__ == "__main__":
    application.run()