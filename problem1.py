#! python3
 
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
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

num = input("Number?:")
num = float(num)

if num%6 == 0 and num%8 != 0 :
    num = round(num)
    num = int(num)
    print(num,"is frue")
else :
    num = round(num)
    num = int(num)
    print(num,"is not frue")

