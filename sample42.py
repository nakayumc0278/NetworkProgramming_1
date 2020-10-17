#sample42.py
#coding: utf-8

def sell(place, price, num):
    print(place,"支店で",num,"社に",price,"万円の販売を行った")
    tt = price * num
    return(tt)

total = sell("東京",100,5)

print("売上は",total,"万円でした")