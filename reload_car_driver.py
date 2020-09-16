import pandas as pd

df = pd.read_excel('car.xlsx', sheet_name=0, index_col=0)
df.head()
df.loc['A_1', 'type']
df.to_excel('car.xlsx')
