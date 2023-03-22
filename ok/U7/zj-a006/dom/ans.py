#!/usr/bin/env python 
# python=
a = list(map(int,input().split()))
a006=a[1]**2-(4*a[0]*a[2])
if a006 ==0:
  x=int(-a[1]/(2*a[0]))
  print(f"Two same roots x={x}")
elif a006 < 0:
  print("No real root")
else:
  x=int((-a[1]+a006)/(2*a[0]))
  y=int((-a[1]-a006)/(2*a[0]))
  if x > y:
    print(f"Two different roots x1={x} , x2={y}")
  else:
    print(f"Two different roots x1={y} , x2={x}")
