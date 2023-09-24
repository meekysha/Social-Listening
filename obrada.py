import pandas as pd

df = pd.read_csv('merged_mart_april.csv')

column_to_remove = 'Unnamed: 0'
df.drop(column_to_remove, axis=1, inplace=True)

df.to_csv('merged_mart_april_modified.csv', index=False)