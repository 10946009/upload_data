#!/usr/bin/env python 
# python=
A,B,C = map(int,input().split())
wsum = 0 #用來放被刪掉的罐子
C = C // B #算出最多只能間距幾個罐子

#最後一題測資的資料太大，不能使用split處理，
st = input() 
temp = "" #暫存
water = []
for i in st:
  if i == " ":
    water.append(int(temp)//B)
    temp = ""
  else:
    temp += i
if temp:
  water.append(int(temp)//B)

for i in range(A):
  while i > 0:
    gap = abs(water[i-1] - water[i])
    if gap >C: #判斷前一個是否超過最大差距
      wsum += (gap-C)
      #超過的話，就把最多的減少
      if water[i-1] > water[i]:
        water[i-1] -= (gap-C)
      else:
        water[i] -= (gap-C)
      i -= 1 #再去判斷前一個
    else: #如果前一個間距判斷沒有被影響就退出
      break
    
print(wsum)
print()
