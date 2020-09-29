#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math
print("enter a number")
x = input()
x = float(x)

x2 = math.sqrt(x)

x3 = x ** (1. / 3)
x3 = round(x3,4)

print(x2)

print(x3)

if x2 == int(x2) and x3 == int(x3):
    print("xx is both a perfect square and a perfect cube.")
elif x2 == int(x2) and x3 != int(x3):
    print("xx is only a perfect square.")
elif x2 != int(x2) and x3 == int(x3):
    print("xx is only a perfect cube.")


