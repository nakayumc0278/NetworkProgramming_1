#sample48.py
#coding: utf-8

a = 0

def func():
	global a
	b = 0
	print("変数a",a,"変数b",b)
	a += 1
	b += 1

for i in range(5):
	func()

