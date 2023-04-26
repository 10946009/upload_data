#!/usr/bin/env python 
# python=
while 1:
  try:
    a,b = map(int,input().split())
    ans=[]
    for i in range(a):
      ans.append(list(input().split()))
    for i in range(b):
      for j in range(a):
        print(ans[j][i],end=" ")
      print()
  except:
    break
