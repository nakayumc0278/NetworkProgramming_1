#sample37.py
#coding: utf-8

cityA = {"東京","名古屋","京都","大阪"}
cityB = {"京都","大阪","福岡"}

print("Aの都市名は",cityA)
print("Aの都市名は",cityB)

print("共通するデータは",cityA & cityB)
print("Aのみのデータは",cityA - cityB)
print("Bのみのデータは",cityB - cityA)
print("全てのデータは",cityA | cityB)
print("どちらか一方のデータは",cityA ^ cityB)