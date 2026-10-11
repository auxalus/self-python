# reverse a number
# take number by user input

n = int(input('Enter a number : '))

reverse = 0
num = abs(n)

while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

if n < 0:
    reverse = -reverse

print('Reversed number is :', reverse)

