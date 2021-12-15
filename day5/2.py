#Write a Python program to convert temperatures to and from celsius, fahrenheit.
A=int(input("Enter the temperature in fahrenheit or celsius: "))
C = (5/9) * (A -32)
D=A*(9/5)+32
print(f"{C} celsius", )
print(f"{D} fahrenheit")