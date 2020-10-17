#sample34.py
#coding: utf-8

sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale)

print("キーを表示")
for k in sale.keys():
    print(k,end="\t")
print()

print("値を表示")
for v in sale.values():
    print(v,end="\t")
print()

print("キーと値を表示")
for i in sale.items():
    print(i,end="")
print()