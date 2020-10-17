#sample27.py
#coding: utf-8

city = ["東京","名古屋","大坂","京都",]
sale = [80,60,22,50,75]

print("都市名データは",city)
print("売上データは,sale")

print("データを組み合わせ")

for i in zip(city,sale):
	print(i)

print("データを分解する")

for c, s in zip(city,sale):
		print("都市名は",c,"売上は",s)

