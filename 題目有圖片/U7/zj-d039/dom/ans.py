#!/usr/bin/env python 
# python=
for i in range(int(input())):
  a,b = map(int,input().split())
  print((a//3)*(b//3) if (a//3)*(b//3) != 0 else 1)
