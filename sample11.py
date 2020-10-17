#sample11.py
#coding: utf-8

sale = int(input("売り上げを入力"))
num = int(input("人数を入力"))

if sale >= 100 and num >= 50:
	print("売上は大盛況")
elif sale >= 100:
	print("売上は好調")
elif sale >= 50:
	print("売上は普通")
else:
	print("売上は低調")
