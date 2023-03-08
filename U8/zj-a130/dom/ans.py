#!/usr/bin/env python 
# python=
for i in range(int(input())):
  print(f"Case #{i+1}:")
  ans_list = []
    #讀取資料
  for n in range(10):
    url,a = input().split(" ")
    ans_list.append([int(a),url])
     #進行判斷
  max_math = max(ans_list)[0]
  for i in ans_list :
    if i[0] == max_math:
      print(i[1])
