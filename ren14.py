#ren14.py
#coding: utf-8

def rpstr():
	str = "*"
	str1 = input("文字列を入力")
	num = int(input("個数を入力"))
	
	print("文字列あり",end="")
	for i in  range(num):
		print(str1,end="")

	print()
	print("xxxxxxxxx")
	
	print("文字列なし",end="")
	for i in  range(num): 
		print(str,end="")
	print()

rpstr()