#!/usr/bin/env python 
# python=
lst = []
nmax = 1000000
for i in range(1,nmax+1):
  a = list(map(int,str(i)))
  temp = sum(a) + i
  if temp <= nmax:
    lst += [temp]
numlst = list(range(1,nmax+1))
newlst = set(numlst) ^ set(lst)
# #把,跟[]刪掉 直接印出來
print(str(newlst)[1:-1].replace(', ','\n'))
# 或是用下面這個print也可以
# for i in newlst:
#   if i <= nmax :
#     print(i)
