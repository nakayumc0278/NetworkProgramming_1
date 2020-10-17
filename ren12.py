#ren12.py
#coding: utf-8

citys = ["東京","名古屋","大阪","京都","福岡"]

Cmax = [32,28,27,26,27]
Cmin = [25,21,20,19,22]

print("最高気温は",Cmax)
print("最低気温は",Cmin)

for city, max, min in zip (citys,Cmax,Cmin):
	print(city,"の最高気温は",max, "最低気温は",min)

