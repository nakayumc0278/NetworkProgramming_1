#renfunc02.py
#coding: utf-8

def vote():
    vote_num = 0
    print("投票開始")
    val = 0
    while True:
        vote_num = int(input("選択してください(1-投票 2-票数 0-箱を空 9-終了)"))
        if vote_num == 1:
            val +=1
            print("投票します")
        elif vote_num == 2:
            print("票の数は",val)
        elif vote_num == 0:
            val = 0
            print("票の数は",val)
        elif vote_num == 9:
            print("処理終了")
            break
        else:
            print("正しい値を入力してください")

vote()