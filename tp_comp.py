# -*- coding: utf-8 -*-
vec = [-4, -2, 0, 2, 4]
v1 = [x*2 for x in vec]
v2 = [x*2 if x >= 0 else '' for x in vec ]
v3 = [x*2 for x in vec if x >= 0 else ''  ]


a=0

b =1 if a==0 else 2

if a==0:
    b=1
else: 
    b=2

print(v2)   
