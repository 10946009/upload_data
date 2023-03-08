#!/usr/bin/env python 
# python=
for i in range(int(input())):
  num = int(input())
  count = 0
  while 1 :
    
    numlst = list(str(num))
    if numlst[::-1] != numlst or count == 0 :
      num += int(str(num)[::-1])
      count += 1
    else: 
      break
    
  print(count,num)
