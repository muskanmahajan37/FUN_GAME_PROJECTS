# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:46:18 2019

DEVELOPER ROHAN
"""
print("="*40)
number=[21,32,45,67,87,90,22,12]
print(number)
print('''
press 1 to find the maximum number in the list
press 2 to find the minimum number in the list''')
choice=raw_input("enter your choice : ")
if choice=='1':
    max=number[3]
    for i in number:
        if i>max:
            max=i
    print("the maximim values from the list is : ")
    print(max)
elif choice=='2':
    min=number[0]
    for j in number:
        if j<min:
            min=j
    print("the minimum value from the list is : ")
    print(min)
else:
    print("you have entered the wromg choice..enter the right choice..")    