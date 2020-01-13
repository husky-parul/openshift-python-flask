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



@application.route("/memory")
def lotsofmemory():
    # do a lot of memory work
    for i in range(200):
        arr = [[1]*20 for i in range(2000)]
        # print(len(arr[100]))
        arr1 = [[1]*20 for i in range(2000)]
        # print(len(arr1[110]))
        arr2 = [[1]*20 for i in range(2000)]
        # print(len(arr2[210]))
        arr3 = [[1]*20 for i in range(2000)]
        # print(len(arr3[310]))
        arr4 = [[1]*20 for i in range(2000)]
        # print(len(arr4[410]))
        arr5 = [[1]*20 for i in range(2000)]
        # print(len(arr5[510]))
    
    lengths = "arr =  " + str(len(arr)) + "arr1 =  " + str(len(arr1)) + "arr2 =  " + str(len(arr2)) + "arr3 =  " + str(len(arr3)) + "arr4 =  " + str(len(arr4)) + "arr5 =  " + str(len(arr5))

    return jsonify(lengths)
    


if __name__ == "__main__":
    application.run()