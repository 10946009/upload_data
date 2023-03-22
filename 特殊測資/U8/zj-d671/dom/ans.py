#!/usr/bin/env python 
# python=
for i in range(int(input())):
  s = list(input())
  if int(len(s)**0.5)**2 != len(s) :
    print("INVALID")
  else: 
    slst = []

    for index , j in enumerate(s) :
      if index == int(len(s)**0.5) :
        break
      
      for k in range(index,len(s),int(len(s)**0.5)):
        print(s[k],end = "")
    print()
