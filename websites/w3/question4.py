# Read a number from input.
# Print its multiplication table from 1 to 10.
# Each line should look like this:
# [number] x [i] = [result]

n = int(input("num here"))

for i in range(1,11):
  print(n," X ", i ," = ", i*n)