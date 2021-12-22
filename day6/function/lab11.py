# Write a program to find the factorial of a number using functions.
'''
def factorial(n):
 if(n==0 and n==1):
  return 1
 f=n*factorial(n-1)
 return f
 '''

#
def fact(): 
	num = input("enter a number : ") 
	fact = 1 
	i = 1 
	while i <= num: 
		fact = fact * i 
		i=i+1 
	 
	print ("factorial of the number : %d" %fact) 
 
fact() 