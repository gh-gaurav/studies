from pyspark.sql import SparkSession # type: ignore

# Initialize Spark session
spark = SparkSession.builder.appName("ReadTextFile").getOrCreate()

# Absolute path to the text file
file_path = r"G:\studies\pyspark\textfile.txt"

# Reading text file and creating RDD
rdd = spark.sparkContext.textFile(file_path)

# Print the contents of the file
for line in rdd.collect():
    print(line)


# Perform some basic RDD operations
print(f"Number of lines in the file: {rdd.count()}")
print(f"First line in the file: {rdd.first()}")

print(type(rdd))
# Stop the Spark session
spark.stop()
