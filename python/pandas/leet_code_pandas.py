#User
# task -1 
# Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
import pandas as pd
list = [
    [1,200],
    [2,300],
    [3,400],
    [4,400],
    [5,500],
    [6,600],
    [7,]
    ]

df = pd.DataFrame(list,columns=['student_id','age'])
# print(df)

#task -2
#return the size of rows and colums in a list

# rows,columns = df.shape
rows = df.shape[0]
columns = df.shape[1]
# print([rows,columns])


#task -3
#data where student id =3
# print(df[df['student_id']==3])


#task-4

#creating new column to existing dataframe
# df['bonus'] = (df['age'])*2
# print(df)


#task 5
#dropping duplicates values

# df.drop_duplicates(subset='age',keep='first',inplace=True)
# df.reset_index(drop =True ,inplace=True)
# print(df)


#second method
# df1 = df.groupby('age').first().reset_index()

# df1 = df1[['student_id','age']]
# print(df1)

#task 6
#There are some rows having missing values in the name column.

#Write a solution to remove the rows with missing values.

df2 = df.dropna(subset='age')
# print(df2)
# print(df)

#task 7
#renaming a column

#soln1
# df2.columns = ['id','age']

#soln2
# df2.rename(columns={'student_id':'id','age':'ages'},inplace=True)


#task 8
#changing datatype of column
# print(df2.dtypes)

# df2['age'] = df2['age'].astype(int)
# print(df2.dtypes)


#task 9
#fill up the none value to lets say 0
# df['age'].fillna(0,inplace = True)
# print(df)

data1 = {
    'Names': ['Gaurav','Shivam','Medinee','Anjali'],
    'City':['indore','mhow','rewa','balaghat'],
    'cgpa':[10,9,7,8]
}

data2 = {
    'Names': ['Mayur','Pranjal','Priya','Sakshi'],
    'City':['indore','kannuj','indore','harda'],
    'cgpa':[6,9,10,8]
}

student1 = pd.DataFrame(data1)
student1.index += 1

student2 = pd.DataFrame(data2)
student2.index += 1

# print(student1)
# print(student2)

student = pd.concat([student1,student2]).reset_index(drop = True)
student.index += 1
print(student)