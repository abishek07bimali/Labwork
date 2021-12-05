#Given a positive real number, print its fractional part. 
import math
A=float(input("Enter the First number: "))
x,y= math.modf(A)
print(x)
print(y)