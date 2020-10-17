#sample47.py
#coding: utf-8

a = 0

def funcA():
	global x
	b = 1
	x = 100

	print("funcAのなかでは変数aと変数bが使える")
	print("変数aの値は",a)
	print("変数bの値は",b)
	print("変数xの値は",x)
def funcB():
	c = 2
	print("変数aの値は",a)
	print("変数cの値は",c)
	print("変数xの値は",x)

print("関数の外では変数aが使える")
funcA()
funcB()

print("global文の変数xは関数外で使える")
print("変数xの値は",x)
