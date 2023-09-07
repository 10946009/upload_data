#!/usr/bin/env python 
# python=
while 1:
  try:
    a = list(map(int,(input().split())))
    print("0" if (sum(a)-a[0])/a[0] > 59 else "1")
  except:
    break
