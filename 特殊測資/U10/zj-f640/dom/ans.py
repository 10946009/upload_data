#!/usr/bin/env python 
# python=
def f(x):
  x = int(x)
  return 2 * x - 3
def g(x, y):
  x = int(x)
  y = int(y)
  return 2*x + y - 7
def h(x, y, z):
  x = int(x)
  y = int(y)
  z = int(z)
  return 3*x - 2*y + z

def l(lst):
  if len(lst) == 1:
    return print(lst[0])
  for index , i in enumerate(lst) :
    if i == 'f':
      lst[index-1] = f(lst[index-1])
      lst.remove('f')
      break
    if i == 'g':
      lst[index-2] = g(lst[index-1],lst[index-2])
      lst.remove('g')
      lst.pop(index-1)
      break
    if i == 'h':
      lst[index-3] = h(lst[index-1],lst[index-2],lst[index-3])
      lst.remove('h')
      lst.pop(index-1)
      lst.pop(index-2)
      
      break
  l(lst)
a = list(input().split())
a.reverse()
l(a)
