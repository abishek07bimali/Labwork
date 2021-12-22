# Write a Python function that takes a number as a parameter and check the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors 
#other than 1 and itself.
n=int(input("Enter the number: "))
if n==1:
    print("1 is not a prime number")
else:
    x=2
    flag=False
    while x<=n//2:
        t=n%x
        if t==0:
            flag=True
        x+=1
    if flag==False:
        print(n," is a prime number")
    else:
        print(n," is not a prime number")
