# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

# number of rows
def row(rows):
    for i in range(0, rows):
        for j in range(0, i + 1):
            print("*", end=' ')
        print(" ")
row(5)
