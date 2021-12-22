#Write a Python function to find the Max of three numbers.


def max(x,y,z):
    if x>y>z:
        print(x)
    elif y>x>z:
        print(y) 
    else:
        print(z)
max(2,3,4)