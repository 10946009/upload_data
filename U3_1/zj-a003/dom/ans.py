#!/usr/bin/env python 
# python!=
a=input().split()
b=(int(a[0])*2+int(a[1]))%3
if b==0:
    print("普通")
elif b==1:
    print("吉")
else:
    print("大吉")
