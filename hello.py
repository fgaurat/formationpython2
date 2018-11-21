# -*- coding: utf-8 -*-


squares = [1, 4, 9, 16, 25]
# print(squares)

a=1
b=a

ref_squares = squares
val_squares = squares[:] 


# ref_squares[0]=52
# print("ref_squares",ref_squares)
# print("squares",squares)

# val_squares[0]=22
# print("val_squares",val_squares)
# print("squares",squares)

arr_1 = [1,2]
arr_2 = [3,4]
arr = [arr_1,arr_2]
val_arr = arr[:] 
arr_1[0]=22
print("arr",arr)
print("val_arr",val_arr)
val_arr.append(7)
print("val_arr",val_arr)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C']

print(letters)