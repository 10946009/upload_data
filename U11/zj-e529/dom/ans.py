#!/usr/bin/env python 
# python=
for n in range(int(input())):
  input()
  index = list(map(int,input().split()))
  lst = list(input().split())

  zipped = list(zip(index,lst))
  zipped.sort()
  for i in zipped:
    print(i[1])
