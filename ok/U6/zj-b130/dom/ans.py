#!/usr/bin/env python 
# python=
input()
a = list(set(map(int,input().split())))
a.sort()
print(len(a))
for i in a:
  print(i,end=' ')
