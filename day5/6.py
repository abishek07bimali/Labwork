# Write a Python program to count the number of even and odd numbers from a series of numbers.
A=range(11)
odd=0
even=0
for digit in (A):
    if digit %2==0:
        even+=1 
    else:
        odd+=1
print("even number are :",even)
print(f"odd number are: {odd}")