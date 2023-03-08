#!/usr/bin/env python 
# python=
a = [] 
lst = []
n,l = map(int,input().split())
lsum = 0
for j in range(n):
  x,i = map(int,input().split())
  a.append([i,x])
a.sort()
lst.append(0)
lst.append(l)
  #經過排序

for k in a:
  lst.append(k[1])
  lst.sort() #放入0到7之間
  lsum += lst[lst.index(k[1])+1] - lst[lst.index(k[1])-1]  #找到放入的數字 抓前後的距離 
  

print(lsum)
