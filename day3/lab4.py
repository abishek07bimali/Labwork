#Given three integers, print the smallest one. (Three integers should be user input) 
A=int(input("Enter the First number: "))
B=int(input("Enter the Second number: "))
C=int(input("Enter the Third number: "))
if A>B>C:
    print("A is the greatest.")
elif B>C>A:
    print("B is the greatest.")
else:
    print("C is the greatest.")