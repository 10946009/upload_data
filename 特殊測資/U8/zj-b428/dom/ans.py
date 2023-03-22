#!/usr/bin/env python 
# python=
while 1:
  try:
    a = list(input())
    b = list(input())
    if ord(b[0])-ord(a[0])>0:
      print(ord(b[0])-ord(a[0]))
    else:
      print(((ord(b[0])-ord(a[0]))+26)%26)
  except:
    break
