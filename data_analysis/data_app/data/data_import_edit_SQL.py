import sqlite3
import csv

"""
Leave all program lines active until data will be transfared end edited in database.
"""


"""DATA IMPORT/EDITING IN DATABASE"""

"""Creating a connection to the database"""
# conn = sqlite3.connect('db.sqlite3')

"""Creating a cursor object"""
# c = conn.cursor()

"""Reading data from the CSV file"""
# csv_file = open('edited_temp_data.csv')
# contents = csv.reader(csv_file)

"""Inserting data into db table"""
# with conn:
#     insert_records = "INSERT INTO data_app_temperature ('region','country', 'city', 'year', 'month', 'avg_temp_F' ) VALUES (?,?,?,?,?,?)"
#     c.executemany(insert_records, contents)

"""Editing data in the db table"""
# with conn:
#     c.execute("DELETE FROM data_app_temperature WHERE region='Region'")
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