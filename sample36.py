#sample36.py
#coding: utf-8

city = {"東京","名古屋","京都","大阪","福岡"}
print("現在のデータは",city)

k = input("追加するデータを入力してください")
if k in city:
    print(k,"のデータは既に存在しています")
else:
    city.add(k)
    print(k,"を追加しました")
print("現在のデータは",city)

k = input("削除するデータを入力してください")
if k in city:
    city.remove(k)
    print(k,"を削除しました")
else:
    print(k,"のデータが見つかりません")
print("現在のデータは",city)
