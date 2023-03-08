#!/usr/bin/env python 
# python!=
a = int(input())
print("a leap year" if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else "a normal year" )
