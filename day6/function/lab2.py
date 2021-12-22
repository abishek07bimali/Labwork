#No.2 Write a function called fizz_buzz that takes a number.
#If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.
#If it is divisible by both 3 and 5, it should return “FizzBuzz”. Otherwise, it should return the same number.

def fiz_buzz():
    for i in range(51):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print("buzz")
            continue
        print(i)
fiz_buzz()

