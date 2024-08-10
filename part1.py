import pandas as pd

df = pd.read_csv('final_data.csv')
print(df.head())

print(df.info())

print(df.describe())