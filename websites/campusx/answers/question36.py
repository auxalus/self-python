# Print all factors of a number provided by the user

n = int(input('enter a number'))
temp = 1
for i in range(1,n+1):
  temp *= i
print(temp)