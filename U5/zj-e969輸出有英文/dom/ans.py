#!/usr/bin/env python 
# python=
a = list(map(int,input().split()))
money= a[0]
time= a[1]
sumtime = 0
food = a[2]
foodtable = {1:"drinks a Corn soup",
        0:"eats an Apple pie"}
while 1:
  if food == 1 and money >=55:
    money -= 55
  elif food ==0 and money >=32:
    money -= 32
  elif sumtime == 0:
    print("Wayne can't eat and drink.")
    break
  else:
    break

  if money == 0:
    print(f"{sumtime}: Wayne {foodtable[food]}, and now he doesn't have money.")
    break
  if money == 1:
    print(f"{sumtime}: Wayne {foodtable[food]}, and now he has {money} dollar.")
  else:
    print(f"{sumtime}: Wayne {foodtable[food]}, and now he has {money} dollars.")
  sumtime += time
  food = 1 - food
