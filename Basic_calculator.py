#Basic calculator

import math

global num1
global num2
global opr

num1 = ''
num2 = ''
opr = ''

def add():
    print(float(num1+num2))

def sub():
    print(float(num1-num2))

def dev():
    if num1 == '0' or num2 == '0':
        raise(ZeroDivisionError)
    else:
        print(float(num1/num2))

def mul():
    print(float(num1*num2))

def per():
    print(float(num%num2))

num1 = float(input("Enter the 1st num: \n"))
num2 = float(input("Enter The 2nd num: \n"))
opr = input("Enter the operation: \n")

if opr == '+':
    add()

elif opr == '-':
    sub()

elif opr == '/':
    dev()

elif opr == '*':
    mul()

elif opr == '%':
    per()

else:
    print("Operation not found!")