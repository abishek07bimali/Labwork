'''
2. WAP which accepts marks of four subjects and display total
 marks, percentage and grade. Hint: more than 70% –> 
distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
'''
A=int(input("Enter the marks of maths: "))
B=int(input("Enter the marks of English: "))
C=int(input("Enter the marks of Science: "))
D=int(input("Enter the marks of Nepali: "))
Total_marks=A+B+C+D
print(f"The total marks is {Total_marks} ")
Percentage=Total_marks/4
print(f"The percentage obtaine is {Percentage}% : ")
if Percentage>70:
    print("you obtained distinction.")
elif Percentage>60:
    print("you obtained FIrst division.")
elif Percentage>40:
    print("you are pass.")
else:
    print("you are fail.")

