#!/usr/bin/env python3
#coding: utf-8

import itertools

#解読したい単語を入れる
word = input('解読したい単語を入力: ')
print('解読中...')

#分割（重複は削除）
separated = list(set(word))
#print(separated)

##何分割するか計算
#length = len(separated)
#print(str(length) + '分割')

#並べ替え
for v in itertools.permutations(separated):
    print(''.join(v))



