#!/usr/bin/env python 
# python=
i = 0
for k in range(int(input())):
  a = int(input())
  lst = [a]
  temp = a
  try:
    while 1:
      switch = 1
      if 1 in lst:
        i += 1
        print(f"Case #{i}: {a} is a Happy number.")
        break
      for j in list(map(int,str(temp))):
        if switch :
          temp = 0
          switch = 0
        temp += j**2
      if temp in lst :
        i += 1
        print(f"Case #{i}: {a} is an Unhappy number.")
        break 
      lst.append(temp)
  except:
    break
