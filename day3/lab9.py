#take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".


for i in range(3):
    A=input("enter the username: ")
    if (A)=="Abishek":
        B=int(input("enter the password: "))
        if (B)==123456:
            print("Logged in")
            break
        else:
                print("invalid password")
    else:
        print("Invalid usernames")
else:
    print("enter")