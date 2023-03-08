#!/usr/bin/env python 
# python=
while 1:
  i = int(input())
  if i == 0 :
    break
  print(f"f91({i}) = {i-10}" if i >= 101 else f"f91({i}) = 91")
