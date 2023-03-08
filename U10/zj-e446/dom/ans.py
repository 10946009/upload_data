#!/usr/bin/env python 
# python=
from itertools import permutations
lst = list(map(str,range(1,int(input())+1)))
s = permutations(lst)
for i in s :
  print(' '.join(i))
