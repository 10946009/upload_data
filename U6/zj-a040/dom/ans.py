#!/usr/bin/env python 
# python=
a,b = map(int,input().split())
no = 1
for i in range(a,b+1):
  s = str(i)
  s_sum = 0
  #計算阿姆斯壯數
  for j in range(len(s)):
    s_sum += int(s[j])**len(s)
  
  #符合條件就印
  if s_sum == int(s) :
    no = 0
    print(s_sum , end=' ')

if no:
  print("none")
