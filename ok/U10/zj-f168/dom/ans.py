#!/usr/bin/env python 
# python=
from itertools import combinations
switch = 0
input()
a = list(map(int,input().split()))
avg = sum(a)//3
lst = []
newlst = []
for i in range(len(a)+1) :
  b = list(combinations(a,i+1))
  for j in b:
    if sum(j) == avg :
      lst.append(list(j))

combilst = list(combinations(lst,3))
for i in combilst:
  if len(i[0])+len(i[1])+len(i[2]) == len(a):
    for j in i :
      for k in j :
        newlst.append(k)
    
    newlst.sort()
    a.sort()
    if newlst == a :
      switch = 1
      break  
    newlst = []
print("1" if switch else "0")

