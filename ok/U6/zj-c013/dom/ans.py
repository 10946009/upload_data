#!/usr/bin/env python 
# python=

input()
input()
while 1:
  try:
    a = int(input())
    b = int(input())
    
    #重複幾個波
    for j in range(0,b):
        
      #往上的波  
      for i in range(1,a+1):
        for k in range(0,i):
          print(i,end='')
        print() 
    
        #往下的波
      for i in range(a-1,0,-1):
        for k in range(0,i):
          print(i,end='')
        
        print()
      print()
  except:
    break
