from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

# Create DataFrame
data = [("John", 28), ("Anna", 23), ("Mike", 32)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Stop the Spark session
spark.stop()
