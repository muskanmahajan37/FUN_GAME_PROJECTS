import os
import time
import datetime
import csv

birthdayFile = 'C:\\Users\\ag16000\\Desktop\\birthdays.txt'


# now = datetime.datetime.now()
# print(now.strftime("%d//%B"))

def Birthdays():
    Name = open(birthdayFile, 'r')
    now = time.strftime('%d/%m')
    print(now)
    flag = 0
    for line in Name:
        if now in line:
            line = line.split(' ')
            # print(line)
            flag = 1
            # line[1] contains Name and line[2] contains Surname
            print('tomorrow is : ' + line[0] + ' birthday')
    if flag == 0:
        print("No Birthdays Tomorrow!")


if __name__ == '__main__':
    Birthdays()
