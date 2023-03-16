#!/usr/bin/env python 
# python=
from itertools import accumulate
while int(input()):
  a = list(map(int,input().split()))
  temp = 0
  while 1:
    a.sort()        #從小到大排序，找出最小的兩個
    temp += a[0] + a[1] #把1+2的結果放進去
    a[0] += a[1]     #把1+2的結果代替第一位
    a.pop(1)       #把第二位移除，因為已經相加過了
    if len(a)== 1:   #如果剩一個就退出
      break
  print(temp)
