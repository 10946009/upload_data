#!/usr/bin/env python 
# python=
while 1:
  try:
    a = int(input())
    sum=0
    for i in range(1,a):
      if a % i == 0:
        sum += i
    if a == sum:
      print("完全數")
    else:
      print("虧數" if a > sum else "盈數")
  except:
    break
