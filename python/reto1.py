
"""
Here is a sample line of code that can be executed in Python

print("Hello, World!")

You can just as easily store a string as a variable and then print it to stdout:

my_string = "Hello, World!"
print(my_string)

The above code will print Hello, World! on your screen. Try it yourself in the editor below!
You do not need to read any input in this challenge.
"""

print("Hello, World!")

"""
Given  an integer, n, perform the following conditional actions:

If n  is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

"""




#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:        
        if n >= 2 and n<=5:
            print("Not Weird")
        elif n >= 6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
    else:
        print("Weird")        


"""

The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print(a-b)
    print(a*b)
