from pyspark.sql import SparkSession #type: ignore

# Initialize Spark session
spark = SparkSession.builder.appName("ReadCSVFile").getOrCreate()

# Absolute path to the CSV file
file_path = r"G:\studies\pyspark\test2.csv"

# Reading the CSV file and creating a DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)
#inferschema basically tries to determine the most appropriate datatypes for column
#when true it will treate age as integer but if false then it wil treat as string

# Show the contents of the DataFrame
df.show()

# Print the schema of the DataFrame
df.printSchema()
print(type(df))
# Stop the Spark session
spark.stop()
