#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

n1 = input("first integer")
n2 = input("second integer")
n3 = input("third integer")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

big = max(n1,n2,n3)
sma = min(n1,n2,n3)
if n1 == big and n2 == sma:
    mid = n3
if n2 == big and n3 == sma:
    mid = n1
if n3 == big and n1 == sma:
    mid = n2
if n1 == big and n3 == sma:
    mid = n2
if n2 == big and n1 == sma:
    mid = n3
if n3 == big and n2 == sma:
    mid = n1



if big**2 == mid**2+sma**2 :
    sma = str(sma)
    mid = str(mid)
    big = str(big)
    print(sma+","+mid+","+big,"form a Pythagorean triple")
else:
    sma = str(sma)
    mid = str(mid)
    big = str(big)
    print(sma+","+mid+","+big,"do not form a Pythagorean triple")


