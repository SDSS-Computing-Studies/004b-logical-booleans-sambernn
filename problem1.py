"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

x = input("Enter a number:")
x = float(x)
x1 = x/6
x2 = int(x1)

y1 = x/8
y2 = int(y1)

if (x1 - x2) == 0 and (y1 - y2) != 0:
    print(x ,end="")
    print(" is frue")
else:
    print(x ,end="")
    print(" is not frue")
