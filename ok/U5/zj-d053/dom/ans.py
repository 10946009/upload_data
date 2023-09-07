#!/usr/bin/env python 
# python=
while 1:
  try:
    a,b=list(map(int,input().split()))
    print((a*b)-1)
  except:
    break
