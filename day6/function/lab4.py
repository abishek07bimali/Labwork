# Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20

def calculate_sum(a, N): 
  
    m = N / a 
  
    sum = m * (m + 1) / 2
  
    ans = a * sum
  
    print("Sum of multiples of ", a, 
          " up to ", N, " = ", ans) 
  
calculate_sum(7, 49)
