#sample44.py
#coding: utf-8

def append():
    print("データを追加する")

def update():
    print("データを変更する")

def delete():
    print("データを削除する")

list = [append,update,delete]
res = int(input("操作番号を入力(0 - 2)"))

if 0 <= res and res < len(list):
    list[res]()
