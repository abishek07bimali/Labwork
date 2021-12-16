# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
for digit in range(10):
    if digit==0 or digit==4 or digit==5:
        continue
    else:
        print(digit)