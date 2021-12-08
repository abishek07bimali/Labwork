#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
A= int(input("Enter the First integer: ")) 
B= int(input("Enter the Second integer: "))  
C= int(input("Enter the Third integer: "))  
sum=A+B+C
if A==B or B==C or A==C:
    print(f"The sum is 0.")
else:
    print(f"the sum is {sum}")

