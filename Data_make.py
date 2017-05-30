# -*- coding: utf-8 -*-
import datetime
import os
import shutil
import sqlite3
import numpy as np
#data copy and rename
name = 'race.db'
today = datetime.datetime.now()
current_dir = '/Users/kajiyama/PycharmProjects/keiba_test'
os.chdir(current_dir)
today = "{0:%Y%m%d_%H%M%S}".format(today)
database_name = 'race' + today + '.db'

read_db_dir = os.path.join(current_dir, 'race.db')
write_db_dir = os.path.join(current_dir + '/database', database_name)
shutil.copyfile(read_db_dir, write_db_dir)

os.chdir(current_dir)
os.chdir('database')

'''
#SQL operate
con = sqlite3.connect(database_name)
cur = con.cursor()
race_info = "select id, distance,weather ,race_number from race_info"
sql = "select race_id, horse_number,age ,dhweight,hweight,sex,weight   from feature"
cur.execute(race_info)
# cur.execute(sql)
race_data = []
'''
'''
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
'''

con = sqlite3.connect(database_name)
cur = con.cursor()
sql = "select race_id from race_result"
cur.execute(sql)
race_number = (max(max(cur)))


horse_number_of_race = []
for i in range(race_number):
    sql = "select count(race_id),race_id from race_result where race_id="+str(i+1)
    cur.execute(sql)
    for row in cur:
        horse_number_of_race.append((row[0],row[1]))
        # race_id = row[1]
sorted(horse_number_of_race, key=lambda x: x[1])
print(horse_number_of_race)
max_horse_number = max(horse_number_of_race[:])
# print(max_horse_number[0])
# one_hot_win_horse = np.zeros([race_number,max_horse_number])
# print(one_hot_win_horse)
# con.close()
#     # horse_number_of_race.append(cur[0])
# #
sql = "select race_id, horse_number from race_result where order_of_finish = 1"
cur.execute(sql)
win_data_and_race = []

doutyaku_judge = None
for row in cur:
    #同着防止(同着の場合は少ない数字を一位とする)
    if doutyaku_judge == row[0]:
        pass
    else:
        win_data_and_race.append(row)
        doutyaku_judge = row[0]

sorted(win_data_and_race, key= lambda x:x[0])
print(win_data_and_race)
win_data = []
for win in win_data_and_race:
    win_data.append(win[1])
# print(win_data)
win_data = np.array(win_data)
print(len(win_data))
print(win_data)
b = np.zeros((race_number,max_horse_number[0]))
b[np.arange(race_number), win_data] = 1
print(b)
# def normalization0_to_1(data):
#
