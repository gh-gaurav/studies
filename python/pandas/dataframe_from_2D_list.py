#User
# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
import pandas as pd
list = [
    [1,200],
    [2,300],
    [3,400],
    [4,500],
    ]
df = pd.DataFrame(list,columns = ['student_id','age'])
print(df)