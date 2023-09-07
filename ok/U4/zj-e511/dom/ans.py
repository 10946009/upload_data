#!/usr/bin/env python 
# python=
for i in range(0,int(input())):
  b=input()
  a = list(map(int,input().split()))
  print((max(a)-min(a))*2)
