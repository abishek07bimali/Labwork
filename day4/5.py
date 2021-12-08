'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not.
'''

A=int(input("NUmber of clsss held: "))
B=int(input("NUmber of clsss attended: "))
percent_attend=(B/A)*100
if percent_attend<=75:
    print("You are not allowed to sit in exam.")
else:
    print("You are allowed to sit in exam.")