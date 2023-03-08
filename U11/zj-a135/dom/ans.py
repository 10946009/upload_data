#!/usr/bin/env python 
# python=
dic ={"HELLO" :"ENGLISH",
"HOLA":"SPANISH",
"HALLO":"GERMAN",
"BONJOUR":"FRENCH",
"CIAO":"ITALIAN",
"ZDRAVSTVUJTE":"RUSSIAN"}
i = 0
while 1:
  a = input()
  i+=1
  if a == "#":
    break
  if a in dic:
    print(f"Case {i}: {dic[a]}")
  else:
    print(f"Case {i}: UNKNOWN")
