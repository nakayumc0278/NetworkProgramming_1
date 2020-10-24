#rewiew01.py
#coding: utf-8

country = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "kanagawa"]

data_c = [] 

for i in range(8):
    if len(country[i]) >= 8:
        data_c.append(country[i])

print(data_c)