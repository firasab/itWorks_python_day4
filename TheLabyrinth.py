import sys
import numpy as np
import random
 
life_matrix = []
print("please enter the dim you want thats bigger than 3!")
value = int(input())


for i in range(0,1):
    field = []
    for j in range(0,value):
        x = ("#")
        field.append(x)
    life_matrix.append(field)


for i in range(2,value-1):
    field = []
    x = ("#")
    field.append(x)
    life_matrix.append(field)
    for j in range(1,value-1):
        x = (" ")
        field.append(x)
    x = ("#")
    field.append(x)
    life_matrix.append(field)
   

for i in range(value-1,value):
    field = []
    for j in range(0, value):
        x = ("#")
        field.append(x)
    life_matrix.append(field)

print("Next matrix is the init one:")
for index in life_matrix:
    print(index)