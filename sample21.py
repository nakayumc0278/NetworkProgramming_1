#sample21.py
#coding: utf-8

sale = [80,70,26,50,95]
print("現在のデータは",sale)

print("先頭のデータを削除")

del sale[0]

print("現在のデータは",sale)

print("26を削除")
sale.remove(26)

print("現在のデータは",sale)
