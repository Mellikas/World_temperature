import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Opening data and forming dataframe"""
# df = pd.read_csv('temp_data.csv')

"""DATA CHECKING"""
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())
# print(df.isna().sum())
# print(df['State'].value_counts())

"""unreasonable to leave 'State' data"""
# df = df.drop('State', axis=1)


"""Group by, mean temperature for each day and set a DF world"""
# df2 = df.groupby(['Region', 'Country', 'City', 'Year', 'Month'])['AvgTemperature'].mean().reset_index()
# print (df2.to_string())

"""Looking at year"""
# print(df2['Year'].value_counts())

"""unreasonable to leave not full (2020) and invalid (200;201;) year data"""
# df2.drop(df2[df2['Year'] < 1995].index, inplace=True)
# df2.drop(df2[df2['Year'] > 2019].index, inplace=True)

"""Looking at the AvgTemperature"""
# print(df2['AvgTemperature'].describe())
# ax = sns.barplot(y=df2['AvgTemperature'], x=df2['Year'], data=df2)
# plt.show()



"""Drop negative (<0) temperature values """
# df2.drop(df2[(df2['AvgTemperature'] < -40)].index, inplace=True)
# df2.drop(df2[(df2['AvgTemperature'] < 30) & (df2['Month'] > 2) & (df2['Month'] < 12)].index, inplace=True)


"""Double check for AvgTemperature"""

# print(df2.shape)
# print(df2.info())
# print(df2.isnull().sum())
# print(df2.isna().sum())

"""Save edited data to CSV"""
# df2.to_csv("edited_temp_data.csv", index=False)

"""DATA IMPORT/EDITING IN DATABASE"""

# # creating a connection to the database
# conn = sqlite3.connect('db.sqlite3')
#
# #creating a cursor object
# c = conn.cursor()

# # reading data from the CSV file
# csv_file = open('edited_temp_data.csv')
# contents = csv.reader(csv_file)
#
# # inserting data into db table
# with conn:
#     insert_records = "INSERT INTO data_app_temperature ('region','country', 'city',  'year', 'month', 'avg_temp_F' ) VALUES (?,?,?,?,?,?)"
#     c.executemany(insert_records, contents)

# # editing data in the db table
# with conn:
#     c.execute("SELECT DISTINCT city, country FROM data_app_temperature")
#     c.execute("UPDATE data_app_temperature SET avg_temp_F = ROUND(avg_temp_F,2)")
#     c.execute("UPDATE data_app_temperature SET avg_temp_C = ROUND(((avg_temp_F-32)*5/9),2)")
#     c.execute('UPDATE data_app_temperature SET month_name = "January" WHERE month = "1"')
#     c.execute('UPDATE data_app_temperature SET month_name = "February" WHERE month = "2"')
#     c.execute('UPDATE data_app_temperature SET month_name = "March" WHERE month = "3"')
#     c.execute('UPDATE data_app_temperature SET month_name = "April" WHERE month = "4"')
#     c.execute('UPDATE data_app_temperature SET month_name = "May" WHERE month = "5"')
#     c.execute('UPDATE data_app_temperature SET month_name = "June" WHERE month = "6"')
#     c.execute('UPDATE data_app_temperature SET month_name = "July" WHERE month = "7"')
#     c.execute('UPDATE data_app_temperature SET month_name = "August" WHERE month = "8"')
#     c.execute('UPDATE data_app_temperature SET month_name = "September" WHERE month = "9"')
#     c.execute('UPDATE data_app_temperature SET month_name = "October" WHERE month = "10"')
#     c.execute('UPDATE data_app_temperature SET month_name = "November" WHERE month = "11"')
#     c.execute('UPDATE data_app_temperature SET month_name = "December" WHERE month = "12"')