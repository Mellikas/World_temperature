import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


"""
Leave all program lines active until a new CSV file is created (exception: check lines).
"""


"""DATA OPENING & FORMING DATAFRAME"""
df = pd.read_csv('temp_data.csv', low_memory=False)

"""CHECK: all data"""
# shape = df.shape
# print(f'[(DF) Shape /Dimensionality of DataFrame]: \n {shape} \n ----------------------------------')
#
# head = df.head(10)
# print(f'[(DF) DataFrame head / Columns name check]: \n {head} \n ----------------------------------')
#
# print('[(DF) Info / Summary of a DataFrame]:')
# df.info()
# print(f'----------------------------------')
#
# isnull = df.isnull().sum()
# print(f'[(DF) Is null check]: \n {isnull} \n ----------------------------------')
#
# isna = df.isna().sum()
# print(f'[(DF) Is none check]: \n {isna} \n ----------------------------------')
#
# states = df['State'].value_counts()
# print(f'[(DF) States values check]: \n {states} \n ----------------------------------')

"""DROP: at this project unreasonable to leave 'State' data"""
df.drop('State', axis=1, inplace=True)

"""CHECK: year data"""
# print(df['Year'].value_counts())

"""DROP: unreasonable to leave not full (2020) and invalid (200;201;) year data"""
df.drop(df[df['Year'] < 1995].index, inplace=True)
df.drop(df[df['Year'] > 2019].index, inplace=True)

"""CHECK: avg temperature data"""
# print(df['AvgTemperature'].describe())
# sns.displot(df['AvgTemperature'], height=6, aspect=3)
# plt.show()

"""DROP: unreasonable temperature data (<-40)"""
df.drop(df[(df['AvgTemperature'] < -40)].index, inplace=True)

"""RECHECK: avg temperature data"""
# print(df['AvgTemperature'].describe())
# sns.displot(df['AvgTemperature'], height=6, aspect=3)
# sns.jointplot(x='Month', y='AvgTemperature', data=df)
# plt.show()

"""FORMING NEW DATAFRAME: df2 grouped by ('Region', 'Country', 'City', 'Year', 'Month') on AvgTemperature mean"""
df2 = df.groupby(['Region', 'Country', 'City', 'Year', 'Month'])['AvgTemperature'].mean().reset_index()

"""CHECK: df2 data"""
# shape = df2.shape
# print(f'[(DF2) Shape /Dimensionality of DataFrame]: \n {shape} \n ----------------------------------')
#
# head = df2.head(2)
# print(f'[(DF2) DataFrame head / Columns name check]: \n {head} \n ----------------------------------')
#
# months = df2['Month'].value_counts()
# print(f'[(DF2) Months values check]: \n {months} \n ----------------------------------')

"CHECK: missing city temperature data amounts after unreasonable data deletion. Full data = 25"
# city_months=df2.groupby(by=["City", "Month"]).size().to_string()
# print(f'[(DF2) city_months values check]: \n {city_months} \n ----------------------------------')

"""SAVE EDITED DATA TO CSV"""
# df2.to_csv("edited_temp_data.csv", index=False)