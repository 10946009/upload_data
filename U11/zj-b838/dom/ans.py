#!/usr/bin/env python 
# python=
for n in range(int(input())):
  a = list(input().replace(" ",""))
  i = 0
  count = 0
  while len(a):
    if a[i] == "(" and a[i+1] == ")":
      a.pop(i+1)
      a.pop(i)
      i = 0
      count += 1
    else:
      i += 1

    if len(a) == 0 :
      print(count)
      break
    elif len(a) == 1 or i == len(a) - 1:
      print(0)
      break
