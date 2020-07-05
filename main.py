#!/usr/bin/env python3
#coding: utf-8

import itertools

#解読したい単語を入れる
word = input('解読したい単語を入力: ')
print('解読中...')

#分割（重複は削除）
moji = list(set(word))
separated = list(word)

#何分割するか計算
length = len(separated)

#重複ありで並べ替え結果を入れるリスト
doublist = []

#並べ替えてdoublistにどんどん入れる
for v in itertools.permutations(separated, length):
    doublist.append(''.join(v))

#doublistの中の重複を除いて出力
result = list(set(doublist))
for l in range(len(result)):
    print(result[l])



