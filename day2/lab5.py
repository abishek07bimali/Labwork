classA=int(input("Enter the number of student of class A :"))
classB=int(input("Enter the number of student of class B :"))
classC=int(input("Enter the number of student of class C :"))
deskA=classA%2+classA//2
deskB=classB%2+classB//2
deskC=classC%2+classC//2
print(f"The total number of desk is {deskA+deskB+deskC}")
