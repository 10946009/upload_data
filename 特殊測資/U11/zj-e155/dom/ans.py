#!/usr/bin/env python 
# python=
while 1:
  a = int(input())
  if a == 0 :
    break
  lst = list(range(1,a+1))

  if a == 1:
    print("Discarded cards: ")
    print("Remaining card: 1")
  else:
    print("Discarded cards: ",end = '')
    while a != 1:
      print(f"{lst[0]}, " if len(lst) > 2 else lst[0] , end = '')
    #1.把最上面的牌丟掉(list.pop)
      lst.pop(0)
    #2.把最上面的牌放到最後面(list.append ->list.pop)
      lst.append(lst[0])
      lst.pop(0)
    #3.直到牌剩下最後一張就跳出來(break)
      if len(lst) == 1 :
        break
    print()
    print(f"Remaining card: {lst[0]}")
