#test01.py
#coding: utf-8

i=0
value=0

while value < 99:
	if i == 10:
		print()
		i=0
	value += 3
	i+=1
	print(value,"\t",end="")
print("\n処理終了")