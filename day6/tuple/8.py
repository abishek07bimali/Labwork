#8. Write a Python program to convert a tuple to a string. 
 
def convert(tup):
    str = ''.join(tup)
    return str


A=(1,2,3,4,5,)
print(convert(A))
