#!/usr/bin/env python 
# python!=
hour,min=map(int,input().split())
if hour >= 7 and hour <= 16:
  if hour == 7 and min < 30:
    print("Off School")
  else:
    print("At School")
else:
  print("Off School")
