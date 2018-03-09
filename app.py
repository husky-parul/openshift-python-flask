import os
from pyspark.sql import SparkSession

def produce_pi(scale):
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()
    n = 100000 * scale

    def f(_):
        from random import random
        x = random()
        y = random()
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(
        xrange(1, n + 1), scale).map(f).reduce(lambda x, y: x + y)
    spark.stop()
    pi = 4.0 * count / n
    return pi




def main():
    scale = 2
    print ("We are inside main")
    pi = produce_pi(scale)
    response = "Pi is roughly {}".format(pi)

    print (response)


if __name__ == "__main__":
    print ("This is point 1")
    scale = 2
    print ("We are inside main")
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()
    n = 100000 * scale
    print ("Value of n: ",n)
    def f(_):
        from random import random
        x = random()
        y = random()
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(
        xrange(1, n + 1), scale).map(f).reduce(lambda x, y: x + y)
    spark.stop()
    pi = 4.0 * count / n
    print ("Value of pi: ", pi)
    print ("********* this is the end ****************")
    
    #main()
