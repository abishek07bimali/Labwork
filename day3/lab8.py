# Given a n-digit number. Find the sum of its digits.

A=int(input("Enter the First number: "))
sum=0
for digit in str(A):
    sum +=int(digit)
    print(sum)