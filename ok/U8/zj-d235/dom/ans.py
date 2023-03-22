#!/usr/bin/env python 
# python=
while 1:
  try:
    a = int(input())
    if a == 0:
      break
    print(f"{a} is a multiple of 11." if a % 11 == 0 else f"{a} is not a multiple of 11." )
  except:
    break
