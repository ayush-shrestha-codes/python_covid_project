import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah'],
    'Age': [25, 30, 28, 35, 26, 35, 30, 25],
    'Salary': [55000, 62000, 58000, 72000, 54000, 68000, 60000, 57000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 4.2, 4.1, 3.9, 4.6]
}

df1 = pd.DataFrame(data)

data_2 = {
    'Name': ['alex', 'Bob', 'Charlie', 'Diana', 'Ronaldo', 'Fiona', 'George', 'Harry'],
    'preference': [25, 30, 28, 35, 26, 35, 30, 25],
    'spending': [55000, 62000, 58000, 72000, 54000, 68000, 60000, 57000],
    'Rating': [4.5, 5.0, 3.8, 4.7, 4.2, 4.1, 3.9, 4.6]
}

df2 = pd.DataFrame(data_2)

df_merged = pd.merge(df1, df2, on="Name", how="inner")
print(df_merged)
