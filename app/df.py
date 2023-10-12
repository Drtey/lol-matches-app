from pyspark.sql import SparkSession
import json

def createDataframe(response):
    spark = SparkSession.builder \
    .appName("Fetch API Data") \
    .getOrCreate()
    
    data = json.loads(json.dumps(response))
    
    df = spark.read.json(spark.sparkContext.parallelize([data]))
    df.show()
    
    return df