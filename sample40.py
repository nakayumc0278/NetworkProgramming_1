#sample40.py
#coding: utf-8

def sell(num = 10):
    print(num,"万円の販売")

def func1(a,b,c,d =20,e = 30):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
    print("e=",e)

sell()

print("引数を3個指定")
func1(10,5,15)

print("引数を4個指定")
func1(10,5,15,25)

print("引数を5個指定")
func1(10,5,15,25,35)