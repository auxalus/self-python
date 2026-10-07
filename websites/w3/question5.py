# Create a function that calculates the factorial of that number.
# The factorial of N means: multiply all numbers from 1 to N together.
# Example: factorial of 5 = 1 × 2 × 3 × 4 × 5 = 120
# The factorial of 0 is 1.
# Print the result like this:
# [n]! = [result]



def factorial(n):
    
    total = 1
    for i in range(1,n+1):
      total = total * i
    return total

num = int(input())
print(str(num) + "! = " + str(factorial(num)))