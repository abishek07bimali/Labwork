#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
A=int(input("Enter the number: "))
for x in range(1500,2700):
    if A%7==0 and A%5==0:
        print("the number is divisible by 7 and multiple of 5.")
        break
    else:
        print("Error")
        break
