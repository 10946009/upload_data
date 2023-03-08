#!/usr/bin/env python 
# python=
while 1:
  try:
    a = [1,0,1,1,0,1,1,1,1,1]
    b = [2,3,3,3,2,1,1,3,2,2]
    c = [0,0,1,1,1,1,1,0,1,1]
    d = [2,3,1,3,3,3,2,3,2,3]
    e = [1,0,1,1,0,1,1,0,1,1]
    num_LC = {0 : " ",
          1 : "-"}
    space = " "


    n = list(input().split(" "))
    f = int(n[0])
    number = list(map(int,n[1]))
    if f == 0 and n[1] =="0":
      break
    #第一排
    for i in number:
      print(f" {num_LC[a[i]]*f} ",end = " ")
    print()

    #第二排
    for i in range(0,f):
      for i in number:
        if b[i] == 1:
          print("|",space*f,end = " ")
        elif b[i] == 2:
          print(f"|{space*f}|" ,end = " ")
        elif b[i] == 3:
          print(space*f,"|" ,end = " ")
        else:
          print(space*f+2,end = " ")
      print()
    #第三排
    for i in number:
      print(f" {num_LC[c[i]]*f} ",end = " ")
    print()
    #第四排
    for i in range(0,f):
      for i in number:
        if d[i] == 1:
          print("|",space*f ,end = " ")
        elif d[i] == 2:
          print(f"|{space*f}|" ,end = " ")
        elif d[i] == 3:
          print(space*f,"|" ,end = " ")
        else:
          print(space*f+2,end = " ")
      print()
    #第五排
    for i in number:
      print(f" {num_LC[e[i]]*f} ",end = " ")
    print()
  except:
    break
