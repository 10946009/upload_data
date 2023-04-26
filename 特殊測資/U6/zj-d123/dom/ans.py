#!/usr/bin/env python 
# python=
count = 1
while 1:
  try:
    total = int(input())
    a = list(map(int,input().split()))
    a.sort()
    all = []
    switch = 1
    for i in range(0,total):
      for j in range(i,total):
        sum = a[i]+a[j]
        if sum in all:
          switch = 0
          break
        all.append(sum)


      if not switch:
        print(f"Case #{count}: It is not a B2-Sequence.")
        break

      
    if switch:
      print(f"Case #{count}: It is a B2-Sequence.")
    count += 1
    print()
  except:
    break
