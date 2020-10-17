#sample35.py
#coding: utf-8

sale1 = {"東京":80,"名古屋":60,"京都":22}
sale2 = {"京都":100,"大阪":50,"福岡":75}

print("sale1のデータは",sale1)
print("sale2のデータは",sale2)

print("sale1をsale2で更新")
sale1.update(sale2)
print("sale1のデータは",sale1)