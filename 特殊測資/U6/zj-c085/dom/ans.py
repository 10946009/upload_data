#!/usr/bin/env python 
# python=
case = 1
while 1:
  Z,I,M,L=list(map(int,input().split()))
  firstL = L
  if sum([Z,I,M,L]) == 0:
    break
  Ltotal = list()
  count = 0
  while L not in Ltotal:
      Ltotal.append(L)
      count += 1
      L = (Z*L+I) % M
  if firstL == L:
    print(f"Case {case}: {count}")
  else:
    print(f"Case {case}: {count-1}")
  case += 1
