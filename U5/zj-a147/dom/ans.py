#!/usr/bin/env python 
# python=
while 1 :
  try:
    a = int(input())
    for i in range(1,a):
      print(f"{i} " if i % 7 != 0 else"",end='')
    print()
  except:
    break
