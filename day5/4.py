#Write a Python program that accepts a word from the user and reverse it.
A = input("Input a word to reverse: ")

for char in range((A) - 1, -1, -1):
  print(A[char] , end="")
