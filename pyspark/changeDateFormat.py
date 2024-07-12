from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, to_date

# Initialize Spark session
spark = SparkSession.builder.appName("DateFormatChange").getOrCreate()

# Read the CSV file
file_path = r"G:\studies\pyspark\test3.csv"
df = spark.read.option("header", "true").csv(file_path)

# Convert the date of birth format from MM/dd/yyyy to yyyy-MM-dd
df_with_new_dob_format = df.withColumn("DateOfBirth", date_format(to_date(col("DateOfBirth"), "MM/dd/yyyy"), "yyyy-MM-dd"))

# Show the updated DataFrame
df_with_new_dob_format.show(truncate=False)

# Stop the Spark session
spark.stop()