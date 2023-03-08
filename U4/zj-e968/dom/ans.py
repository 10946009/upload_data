#!/usr/bin/env python 
# python=
people = int(input())
j = list(map(int,input().split()))
for i in reversed(range(1,people+1)):
    if i not in j :
        print(f"No. {i}")
