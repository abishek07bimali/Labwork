#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

for digit in range(6):
    if digit==3 and digit==6:
        continue
    else:
        print(digit)
        