import pandas as pd

df = pd.read_excel('car.xlsx', sheet_name=0, index_col=None)
df.head()


df = pd.read_excel('car.xlsx', sheet_name=0, index_col=0)
df.head()
df.loc['test', 'type'] = 0
df.to_excel('car.xlsx')
