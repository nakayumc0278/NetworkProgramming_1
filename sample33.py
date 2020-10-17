#sample33.py
#coding: utf-8

sale = {"東京":80,"名古屋":60,"京都":22,"大阪":50,"福岡":75}
print("現在のデータは",sale)

k = input("追加するキーを入力してください")
if k in sale:
    print(k,"のデータはすでに存在しています")
else:
    d = input("追加するデータを入力してください")
    sale[k] = d
    print(k,"のデータとして",sale[k],"を追加しました。")
print("現在のデータは",sale)

k = input("どのキーのデータを変更しますか？")
if k in sale:
    print("のデータは",sale[k])
    d = input("データを入力してください")
    sale[k] = d
    print(k,"のデータは",sale[k],"に変更されました。")
else:
    print(k,"のデータは見つかりません")
print("現在のデータ",sale)

k = input("どのキーのデータを削除しますか？")
if k in sale:
    print(k,"のデータは",sale[k])
    del sale[k]
    print("データを削除しました")
else:
    print(k,"のデータは見つかりません")
print("現在のデータ",sale)
