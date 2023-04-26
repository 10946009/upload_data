#!/usr/bin/env python 
# python=
while 1:
  try:
    jolly = list(map(int,input().split()))
    ans = "Jolly"
    jollynum = jolly[1] - jolly[2]
    newjolly = []
    for i in range(1,jolly[0]): #把相減後的成果放進新的list
      if i != len(jolly)-1:
        newjolly.append(abs(jolly[i]-jolly[i+1]))

    for j in range(1,len(newjolly)+1): #判斷是否為n+1或n-1
      if j not in newjolly:
        ans = "Not jolly"

    print(ans)
  except:
    break
