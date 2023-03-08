#!/usr/bin/env python 
# python=
n = int(input())
for i in list(map(int,input().split())):
  if i == 0:
    break
  else:
    print(f"{i // n}" if i % n == 0 else f"{n-(i % n)}")
