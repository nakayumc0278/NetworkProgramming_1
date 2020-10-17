#sample17.py
#coding: utf-8

num = int(input("何月の処理で終了しますか？(1-12)"))

for i in range(12):
	#print(i+1,"月のデータ")
	if (i + 1) == num:
		continue
	print(i+1,"月のデータ")
print("処理終了")
