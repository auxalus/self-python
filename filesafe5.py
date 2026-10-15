# Return the Largest Digit in a Number

n = abs(int(input("Enter a number: ")))
largest_digit = 0

while n > 0:
    digit = n % 10
    if digit > largest_digit:
        largest_digit = digit
    n //= 10

print(largest_digit)