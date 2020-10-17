#sample24.py
#coding: utf-8

sale1 = [1,2,3,4,5,6]
print("上半期のデータは",sale1)

sale2 = [7,8,9,10,11,12]
print("下半期のデータは",sale2)

ysale = sale1 + sale2

print("年間のデータは",ysale)

sale3 = ysale[0:6]
print("上半期のデータは",sale3)

sale4 = ysale[6:]
print("下半期のデータは",sale4)

sale5 = ysale[::2]
print("１ヶ月おきのデータは",sale5)

sale6 = ysale[::-1]
print("逆順のデータは",sale6)

print("年間のデータは",ysale)
print("上半期のデータを更新")
ysale[:6] = [0,0,0,0,0,0]
print("年間のデータは",ysale)
