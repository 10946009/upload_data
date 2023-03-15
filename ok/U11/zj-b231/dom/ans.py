#!/usr/bin/env python 
# python=
asum = 0
alist = []
switch  = 1
tamp = []

for i in range(int(input())):
  a,b = map(int,input().split())
  asum += a
  alist.append([b,a])

alist.sort(reverse=True) #反轉，把最久裝訂時間放在前面

for i in alist:
  #第一欄是裝訂，第二欄是印刷
  if switch:
    switch = 0 #第一個跳過
    continue
#把之前的裝訂時間扣除印刷時間
  tamp = [x - i[1] for x in tamp if x > 0 ]


  tamp.append(i[0])#放入裝訂時間
    
print(max(tamp) + asum)
