#sample46.py
#coding: utf-8

def deco(func):
	def wrapper(x):
		wx = "---" + x + "---"
		return func(wx)
	return wrapper

@deco
def printmsg(x):
	print(x,"入力した")

str = input("メッシージ入力")
printmsg(str)
