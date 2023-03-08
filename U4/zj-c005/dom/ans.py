#!/usr/bin/env python 
# python=
for i in range(0,int(input())): 
  ans=0
  for j in range(0,int(input())):
    people,animal,level=map(int,list(input().split()))
    ans += people*level
  print(ans)
