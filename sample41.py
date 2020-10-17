#sample41.py
#coding: utf-8

def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

func1(1,2,3,4,5)
func2(a=10,b=20,c=30,d=40,e=50)