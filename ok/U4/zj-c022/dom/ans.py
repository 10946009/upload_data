#!/usr/bin/env python 
# python=
for i in range(0,int(input())):
  a=int(input())
  b=int(input())
  sum=0
  for j in range(a,b+1):
    if j % 2 ==1 :
      sum+=j
  print(f"Case {i+1}:",sum)
