#!/usr/bin/env python 
# python=
while 1:
  try:
    a,b = map(int,(input().split()))
    sum = a
    total = a
    while 1:
      if sum // b != 0:
        total+= sum // b
        sum = sum // b + sum % b
      else:
        break
    print(total)
  except:
    break
