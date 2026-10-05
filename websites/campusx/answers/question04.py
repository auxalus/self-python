#find sum of 3 digit number user input

number = int(input('Enter the number : '))

a = number % 10
number = number //10

b = number % 10
number = number //10

c  = number % 10
number = number //10

print(a+b+c)
