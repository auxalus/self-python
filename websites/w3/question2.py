# Read a name and an age from input.

# If the person is 18 or older, print:

# [name] can vote
# If the person is younger than 18, print:

# [name] cannot vote

name = input("your name: ")
age = int(input("your age: "))

# Check and print
if age>=18:
  print(name + " can vote")
else:
  print(name + " cannot vote")