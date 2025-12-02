import pandas as pd
import numpy as np

df = pd.read_csv("data/covid.csv")

'''print(df.head())
print(df.isnull().sum())'''

df = df[['location','date','total_cases','total_deaths','new_cases','new_deaths','population']]
df['date'] = pd.to_datetime(df['date'])
df = df.dropna()
#print(df.tail(20))
#print(df.isnull().sum())

cases_by_location = df.groupby('location')[['total_cases','total_deaths','new_cases','new_deaths']].sum().reset_index()

# Show the top 10 countries with the most confirmed deaths
top_10_cases=cases_by_location.sort_values(by='total_deaths', ascending=False).head(10)

#print(top_10_cases)

cases_by_location['death_ratio'] = np.where(
    cases_by_location['total_cases'] > 0,
    (cases_by_location['total_deaths'] / cases_by_location['total_cases']) * 100,
    0
)

cases_by_location['death_ratio'] = cases_by_location['death_ratio'].round(2)#for simplicity
top10_death_ratio = cases_by_location.sort_values(by='death_ratio', ascending=False).head(10)
print(top10_death_ratio[['location','total_cases','total_deaths','death_ratio']])

#monthly trends
df['year_month'] = df['date'].dt.to_period('M')
print(df['year_month'])
monthly_trends = df.groupby('year_month')[['new_cases','new_deaths']].sum().reset_index()
top10_months = monthly_trends.head(10)
print(top10_months)

#peak montly cases 

# Peak month by new cases
peak_cases_month = monthly_trends.loc[monthly_trends['new_cases'].idxmax()]
print("Peak month by cases:")
print(peak_cases_month)

# Peak month by new deaths
peak_deaths_month = monthly_trends.loc[monthly_trends['new_deaths'].idxmax()]
print("Peak month by deaths:")
print(peak_deaths_month)
