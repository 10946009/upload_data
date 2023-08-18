#!/usr/bin/env python 
# python!=
for i in range(0,int(input())):
  a = int(input())
  print("1" if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else "0" )
