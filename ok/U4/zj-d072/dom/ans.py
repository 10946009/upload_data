#!/usr/bin/env python 
# python!=
for i in range(0,int(input())):
  a = int(input())
  print(f"Case {i+1}: ",end="")
  print("a leap year" if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else "a normal year" )
