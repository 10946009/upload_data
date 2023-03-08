#!/usr/bin/env python 
# python=
number = 0
while 1:
  n = int(input())
  if n == 0:
    break
  teamlist = []
  templist = []
  for i in range(n):
    teamlist.append(list(input().split())[1::])
  queuelist = []
  count = 0
  number += 1
  print(f"Scenario #{number}")
  while n:
    inpu = list(input().split())
    if inpu[0] == "ENQUEUE":
      queuelist.append(inpu[1])

    elif inpu[0] == "DEQUEUE":    
      count = 1
        ##取得第一列的隊伍
      while count:
        if templist == []:
          for i in teamlist:  
            if queuelist[0] in i:
              templist = i
              break
        ##把同個隊伍拿出來
        for i in queuelist:
          if i in templist and count == 1:
            print(i)
            queuelist.remove(i)
            break
        ##如果目前隊伍沒人了
        for i in queuelist:
          if i in templist :
            count = 0
            break
        if count == 1 :
          templist = []
          break
        ##如果已經沒有同個隊伍的了 就要換下組
        if count == 2 :
          templist = []
          count = 0
          break
    elif inpu[0] == "STOP":

      print()
      break
    
