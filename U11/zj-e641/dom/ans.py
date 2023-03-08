#!/usr/bin/env python 
# python=
lst = [[1,"B","F","P","V"],
       [2,"C","G","J","K","Q","S","X","Z"],
       [3,"D","T"],
       [4,"L"],
       [5,"M","N"],
       [6,"R"]]
while 1:
  try:
    n = list(input())
    temp = 0
    for j in n:
      for i in lst:
        if j in i :
          if temp != i[0]: #如果這個英文和前一個不同就印
            print(i[0],end="")
            temp = i[0]
            break
          else:
            break #同樣就跳過
        if i[0] == 6: #如果run到最後一個都沒有就讓暫存歸0
          temp = 0

    print() 
  except:
    break
