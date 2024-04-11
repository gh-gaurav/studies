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

df = pd.DataFrame(list,columns=['student_id','age'])
#return the size of rows and colums in a list

# rows,columns = df.shape
rows = df.shape[0]
columns = df.shape[1]
# print([rows,columns])

#data where student id =3
# print(df[df['student_id']==3])

#creating new column to existing dataframe
print(df)