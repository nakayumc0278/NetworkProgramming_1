#renfunc01.py
#coding: utf-8

def day_func():
    val = int(input("今日からの分類判定"))
    if val == 0:
        print("引数なし 今日")
    elif val == 1:
        print("引数=1 明日")
    elif val == -1:
        print("引数=-1, 昨日")
    else:
        print("今日より１日を超えて離れた日")
day_func()