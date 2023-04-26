#!/usr/bin/env python 
# python=
from itertools import accumulate # 載入 itertools 的 accumulate

while True:
  try:
    n, m = map(int, input().split())
     #將輸入的一連串數字轉成串列
    food = list(map(int,input().split()))   #
    food_sum = [0] + list(accumulate(food))    # 計算總和變成新串列
    #要+0是為了配合索引
    for i in range(m):
      a, b = map(int, input().split())    # 取出前後範圍     
    # 用 0~b 的總和，減去 0~a-1 的總和
      print(food_sum[b] - food_sum[a-1])       
  except:
    break
