#!/usr/bin/env python 
# python=
for a in range(int(input())):
  ans = []
  n = list(map(int,input().split()))
  
  for i in range(0,n[0]):
    ans.extend(list(map(int,input().split())))
  print("go forward" if ans == list(reversed(ans)) else "keep defending")
