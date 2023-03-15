#!/usr/bin/env python 
# python=
for i in range(int(input())):
  A,B,C = map(int,input().split())
  print(f"Case {i+1}: ",end = "")
  if A > 0 and B >0 and C > 0 :
    if A == B and B == C:
      print("Equilateral")
    elif (A+B+C)-max(A,B,C) <= max(A,B,C):
      print("Invalid")
    elif A == B or A == C or B == C :
      print("Isosceles")
    else:
      print("Scalene")
  else:
    print("Invalid")      
