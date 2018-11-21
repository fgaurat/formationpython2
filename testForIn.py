# -*- coding: utf-8 -*-
#!bin/python


words = ['cat', 'window', 'defenestrate']
tmp = words
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)


year = 2018

for i in range(year,year-5,-1):
    print(i)



print(enumerate(words))

for i in enumerate(words):
    print(str(i[0])+" - "+i[1])
