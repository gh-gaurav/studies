from pyspark.sql import SparkSession #type: ignore

#making the spark session

spark = SparkSession.builder.appName("ReadJsonFile").getOrCreate()

file_path = r"G:\studies\pyspark\jsonFile.json"

df = spark.read.json(file_path)
df.show()
spark.stop()