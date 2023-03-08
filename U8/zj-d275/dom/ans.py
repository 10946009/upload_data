#!/usr/bin/env python 
# python=
for i in range(int(input())):
  train = list(input().split()) #把資料放入
  ans = "LOOP"
  tamp = ""

  for i in train:
    #判斷每個軌道長度是否為二
    if len(train) <= 1:
      ans = "NO LOOP"
      break
    
    #判斷是否都是F和M連結
    if tamp != "" and i[0] == tamp :
      ans = "NO LOOP"
      break
    tamp = i[1]
#判斷第一位和最後一位相同，也是NO LOOP
  if (train[0])[0] == (train[-1])[-1]:
    ans = "NO LOOP"
  print(ans) 
