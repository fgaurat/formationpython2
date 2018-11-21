# -*- coding: utf-8 -*-
tel = {'jack': 4098, 'sape': 4139}

print(tel.keys())
print(tel.items())

for key in tel:
    print (tel[key])

a,b= list(tel.items())[0]

print(a,b)

for key in tel.keys():
    print(tel[key])


for key,v in tel.items():
    print( key,v)


print(__name__)