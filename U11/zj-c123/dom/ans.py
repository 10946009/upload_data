#!/usr/bin/env python 
# python=
while 1:
  r = int(input())
  if r == 0 :
    break
  while 1 :
    train = list(range(1,r+1))
    station = []
    lst = list(map(int,input().split()))
    if lst[0] == 0:
      break
    for j in lst:
      while j not in station: #如果這個數字不在車站內
        station = [train.pop(0)] + station #把車站內第一個數字放入
      #如果有了就會跳出來把數字放入
      #如果已經有了，但第一位不符合j，代表順序不可達成
      if station[0] == j:
        station.pop(0)
      else:
        print("No")
        break
    if len(station) == 0:
      print("Yes")
  print()
