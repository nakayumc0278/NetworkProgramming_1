#sample31.py
#coding: utf-8

sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale)

k = input("どの支店のデータを表示しますか?")

if k in sale:
    print(k,"のデータは",sale[k])
else:
    print(k,"のデータが見つかりません")