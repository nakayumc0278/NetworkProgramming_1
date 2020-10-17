#renlist01.py
#coding: utf-8

#area1の値追加
area1 = []
print("area1の入力")
area1.append(int(input("1つめの値を入力")))
area1.append(int(input("２つめの値を入力")))
area1.append(int(input("３つめの値を入力")))
print("現在のarea1の状態",area1)

#area2の値追加
area2 = []
print("area2の入力")
area2.append(int(input("1つめの値を入力")))
area2.append(int(input("２つめの値を入力")))
area2.append(int(input("３つめの値を入力")))
print("現在のarea2の状態",area1)

#結合
print("現在のarea2の状態",area2)
area1.extend(area2)
print("現在のarea1の状態",area1)

#挿入
insert_index = int(input("挿入する位置を入力"))
insert_value = int(input("挿入する値を入力"))
area1.insert(insert_index,insert_value)
print("現在のarea1の状態",area1)

#削除
area1.remove(int(input("消す値->")))
print("現在のarea1の状態",area1)
area1.pop(int(input("消す位置->")))
print("現在のarea1の状態",area1)

#クリア
area1.clear()
print("現在のarea1の状態",area1)