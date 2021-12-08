'''
Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.

if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".

'''
A= (input("Enter the gender (M or F ) :")) 
B= int(input("Enter the age: "))
if (A)=="F":
    print("She will work only in urban areas.")
elif (A)=="M":
    if (B)>=20 and (B)<40:
        print("He can work anywhere.")
    elif (B)>=40 and (B)<60:
        print("He will work in urban area only.")
    else:
        print("Error")
else:
    print("Error")

