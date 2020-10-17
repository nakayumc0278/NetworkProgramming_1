#rendel01.py
#coding: utf-8

val = [1,2,3,4,5,6,7,8,9,10]
print("要素を表示",val)

#要素を削除
for i in range(3):
    del val[len(val)-1]

print("要素の削除後",val)