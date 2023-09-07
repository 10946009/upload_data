#!/usr/bin/env python 
# python=
while 1:
  try:
    a = int(input())
    sum = a
    cola = a
    while cola // 3 != 0:
      if cola // 3 != 0:
        sum += cola // 3
        cola = cola//3 + cola % 3
    print(f"{sum+1}" if cola == 2 else f"{sum}")
  except:
    break
