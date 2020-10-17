#sample19.py
#coding: utf-8

sale = [80,70,26,50,95]
print(sale)

i = 0

i = int(input("何番目のデータを変更しますか？"))
num = int(input("変更後のデータを入力"))

print(i,"番目のデータ",sale[i],"を変更")

sale[i] = num

print(i,"番目のデータは",sale[i],"に変更")

print(sale)
