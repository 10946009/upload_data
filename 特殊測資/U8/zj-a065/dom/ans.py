#!/usr/bin/env python 
# python=
a = list(input())
for i in range(len(a)):
  if i == len(a)-1:
    break
  print(abs(ord(a[i])-ord(a[i+1])), end='')
