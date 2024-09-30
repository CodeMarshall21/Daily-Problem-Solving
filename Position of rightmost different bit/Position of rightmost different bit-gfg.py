#Given two numbers m and n. Find the position of the rightmost different bit in the binary representation of numbers. It is guaranteed that such a bit exists


import math
num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))

exor_val = num1^num2

right_most_set_bit = int(math.log2(exor_val & -exor_val))

print("position of the rightmost different bit : " , right_most_set_bit+1)