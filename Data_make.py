# -*- coding: utf-8 -*-
import datetime
import os
import shutil
import sqlite3

name = 'race.db'
today = datetime.datetime.now()
current_dir = '/Users/kajiyama/PycharmProjects/keiba_test'
os.chdir(current_dir)
today = "{0:%Y%m%d_%H%M%S}".format(today)
database_name = 'race' + today + '.db'
# try:
#     os.chdir('database')
# except:
#     os.mkdir('database')
#     os.chdir('database')
read_db_dir = os.path.join(current_dir, 'race.db')
write_db_dir = os.path.join(current_dir + '/database', database_name)
shutil.copyfile(read_db_dir, write_db_dir)

os.chdir(current_dir)
os.chdir('database')

con = sqlite3.connect(database_name)
cur = con.cursor()
race_info = "select id, distance,weather ,race_number from race_info"
sql = "select race_id, horse_number,age ,dhweight,hweight,sex,weight   from feature"
cur.execute(race_info)
# cur.execute(sql)
race_data = []

for row in cur:
    list_row = list(row)
    if row[2] == "雨" or row[2] =='小雨':
        list_row[2] = -1
    elif row[2] == '晴':
        list_row[2] = 1
    elif row[2] == '曇':
        list_row[2] = 0
    race_data.append(list_row)
print(race_data)
con.close()

# def normalization0_to_1(data):
#
