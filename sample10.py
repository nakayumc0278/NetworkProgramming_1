#sample10.py
#coding: utf-8

sale = int(input("売り上げを入力"))
if sale >= 100:
	print("売上は好調")
elif sale >= 50:
	print("売上は標準")
else:
	print("売上は低調")

print("処理終了")
