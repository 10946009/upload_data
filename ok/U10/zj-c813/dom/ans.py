#!/usr/bin/env python 
# python=
def f(n):
  if sum(n) >= 10 :
    a = list(map(int,str(sum(n))))
    f(a)
  else:
    return print(sum(n))

while 1:
  s = list(map(int,input()))
  if sum(s) == 0 : break
  f(s)
