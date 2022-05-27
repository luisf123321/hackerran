
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


"""
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

No rounding or formatting is necessary.
"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i< n, print i^2.

The list of non-negative integers that are less than n = 3, [0,1,2] Print the square of each number on a separate line.
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

"""

"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')


"""
People who solved List Comprehensions attempted this next:
"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([i,j,k] for i in range(x+1) for j in range(y     +1) for k in range(z+1)  if i+j+k !=n))