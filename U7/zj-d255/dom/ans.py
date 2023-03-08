#!/usr/bin/env python 
# python=
def GCD(a, b):
    if a % b:
        return GCD(b, a % b)
    else:
        return b
