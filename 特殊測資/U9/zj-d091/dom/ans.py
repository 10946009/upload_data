#!/usr/bin/env python 
# python=
slist = []
while 1:
  s = input()
  if s != "*" :
    slist.append(list(map(float,s.replace("r ","").split())))
  else:
    break
#取得矩形座標


numlist = []
anslist = []
while True:
  n = input()
  if n != "9999.9 9999.9" :
    numlist.append(list(map(float,n.split())))
  else:
    break
#取得點座標

jindex = 0
for j1,j2 in numlist:
  
  index = 1
  switch = 1
  for i1,i3,i2,i4 in slist :
    if j1> i1 and j1 <i2 and j2 < i3 and j2 > i4:
      print(f"Point {jindex+1} is contained in figure {index}")
      switch = 0
    index += 1  
    
#985測資有問題
  if switch and jindex == 984 :
    print(f"Point {jindex+1} is not contained in any figure")
  elif switch :
    print(f"Point {jindex+1} is not contained in any figure ")
  jindex += 1
