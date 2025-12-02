import pandas as pd
import numpy as np

df = pd.read_csv("data/covid.csv")

print(df.head())
print(df.isnull().sum())

df = df[['continent', 'Date', 'Deaths', 'Recovered']]
print(df.head())
print(df.columns)
df.rename(columns={'date': 'Date', }, inplace=True)