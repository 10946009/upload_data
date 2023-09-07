#!/usr/bin/env python 
# python=
for number in range(int(input())):
    b = list(map(int,input().split()))
    
    for i in range(len(b)):
        print(b[i],end=" ")

    if (b[1]-b[0]) == (b[3]-b[2]):
        print(b[3]*2-b[2])
    else:
        print(int(b[3]/b[2])*b[3])
