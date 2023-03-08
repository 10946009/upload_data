#!/usr/bin/env python 
# python!=
while 1:
  time = list(map(int,input().split()))
  hour = (time[0] , time[2])
  minu = (time[1] , time[3])
  ansmin = 0
  if hour[1] > hour[0]:
    ansmin += (hour[1] - hour[0])*60
    print(ansmin - (minu[0]-minu[1]))
  elif hour[1] < hour[0]:
    ansmin += (24 - (hour[0] - hour[1]))*60
    print(ansmin - (minu[0]-minu[1]))
  elif sum(time) == 0:
    break
  else:
    print(1440*max(min(minu[0]-minu[1],1),0) - (minu[0]-minu[1]))
