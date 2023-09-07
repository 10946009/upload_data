#!/usr/bin/env python 
# python=
while 1:
  a = int(input())
  if not a:
    break
  print("a leap year" if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else "a normal year" )
