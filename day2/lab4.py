#N students take K apples and distribute them among each other evenly. The remaining
#(the indivisible) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and
#K. It should print the two answers for the questions above.

number_of_students = int(input("The number of students getting apple: "))
number_of_apple = int(input("The number of apple in basket: "))
apple=number_of_apple // number_of_students
remaining=number_of_apple % number_of_students
if apple<=1:
    print(f"All students gets {apple}  apple.") 
else:
        print(f"All students gets {apple}  apples.") 
print( f"The remaining number of apple is {remaining}") 


