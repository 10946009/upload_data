#!/usr/bin/env python 
# python=
import re
for i in range(int(input())):
  st = input().lower()#轉小寫
  st = re.sub(r"[^a-z]","",st) #非英文的刪除
  slst = list(st.replace(" ","")) #放入list


  countlst = [0]*127
  for j in slst:
    countlst[ord(j)] += 1
  cmax = max(countlst)
#次數最多的印出來
  for index,j in enumerate(countlst) :
    if j == cmax :
      print(chr(index),end="")
  print()
