import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

average_salary = df['Salary'].mean()

print(f'Средняя зарплата: {average_salary}')