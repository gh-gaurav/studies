from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Initialize Spark session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read the text file
text_file = spark.read.text(r"G:\studies\pyspark\testfile2.txt")

# Split each line into words and explode into individual rows
words = text_file.select(explode(split(col("value"), "\\s+")).alias("word"))

# Group by words and count the occurrences
word_counts = words.groupBy("word").count()

# Order by count in descending order
ordered_word_counts = word_counts.orderBy(col("count").desc())

# Show all rows in the ordered DataFrame
ordered_word_counts.show(n=ordered_word_counts.count(), truncate=False)

# Stop the Spark session
spark.stop()
