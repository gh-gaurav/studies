import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'keys': ['B', 'D', 'E', 'F'],
                    'value': [3, 4, 5, 6]})

#inner join

# df3 = pd.merge(df1,df2,how='inner',on='key')
# print(df3)

#left join
# df3 = pd.merge(df1,df2,on='key',how = 'left')
# print(df3)


#outer join
df3 = pd.merge(df1,df2,how = 'outer',left_on='key',right_on='keys')
print(df3)