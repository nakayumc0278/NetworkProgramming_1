#renfunc02v2.py
#coding: utf-8

def vote_start(val):
    val = 0
    print("投票開始")
    return val
def vote_add(val):
    val += 1
    print("投票します")
    return val
def vote_check(val):
    print("票の数は",val)
    return val
def vote_reset(val):
    val = 0
    print("票の数は",val)
    return val
def vote_end():
    print("処理終了")

vote = 0
vote_start(vote)

while True:
    vote_num = int(input("選択してください(1-投票 2-票数 0=箱を空 9-終了)"))
    if vote_num == 1:
        vote = vote_add(vote)
    elif vote_num == 2:
        vote = vote_check(vote)
    elif vote_num == 0:
        vote = vote_reset(vote)
    elif vote_num == 9:
        vote_end()
        break
    else:
        print("正しい値を入力してください")