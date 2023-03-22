#!/usr/bin/env python 
# python=
while 1:
  try:
    compare_sum = ans_sum = 0
    a,b = input().split()
    a = int(a)
    blst = list(map(int,b))

    if a != 10 :
      ans_sum = int(b,a) #取得a進位轉十進位
    
#取得數字**長度後的加總
    for j in blst :
      compare_sum += j ** len(blst) 

    print("YES" if ans_sum == compare_sum or compare_sum == int(b) else "NO")
  except:
    break
