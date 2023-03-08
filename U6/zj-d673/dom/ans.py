#!/usr/bin/env python 
# python=
count = 1
while 1:
  try:
    qsum = int(input())
    if qsum == -1:
      break
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(f"Case {count}:")
    for i in range(0,12) :
      if qsum >= b[i] :
        print("No problem! :D")
        qsum = ( a[i] + qsum ) - b[i]
      else:
        print("No problem. :(")
        qsum += a[i]
    count += 1
  except:
    break
