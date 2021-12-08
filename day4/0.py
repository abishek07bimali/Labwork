'''Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else
print ‘COMMON YEAR’.
Hint: • a year is a leap year if its number is exactly divisible by 4 and is not
exactly divisible by 100
• a year is always a leap year if its number is exactly divisible by 400
'''
def CheckLeap(Year):  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year")  
Year = int(input("Enter the number: "))  
CheckLeap(Year)  