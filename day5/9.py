#Write a program to find the factorial of a number.
import math
A=int(input("enter the number: "))
def fun(n):
    return(math.factorial(n))
f=fun(A)
print(f)