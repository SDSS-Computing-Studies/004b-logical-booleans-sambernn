#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
print("enter a number")
x = input()
x = int(x)

if x > 0:
    print("xx is a positive integer.")
elif x < 0:
    print("xx is not a positive integer")