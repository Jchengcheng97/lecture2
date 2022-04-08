#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:11:46 2022

@author: jinchengcheng
"""
import datetime

x = 10
y = 5.1
z = x * y

print(z)
print(type(x))
print(type(y))
print(type(z))
#class: the blueprint of an object

x =100
x = x +15 #assignment
x += 15 # assignment

print(x+15) # no assignment

x = 10
y = 11
print(x == x)
print(x != y)

x = 'abc'
y ='123'
z = x +y
print(z)

my_string = 'hello world!'
big_string = my_string.upper()
print(big_string)
#把所有的变成大写

#把变量变成string
name = 'BOb'
my_string = f'Hello {name}, welcome to class.'
print(my_string)

x = [1, 2, 3]
print(X)
print(len(x))

#list()
#tuple()
#list can assignment
list[0]='A'
#tuple不可以
#set is unique,每个元素不重复
#sets enforce unique values
#sets do not maintian ordering

my_string = 'hello world!'
print(my_string[::-1])
#倒过来

#dictionary
my_dict = {'a':100, 'b':200}
print(my_dict['a'])
#100

my_date = datetime.datetime(2020,3,1)
print(my_date)
