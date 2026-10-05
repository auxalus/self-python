#Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

a = int(input("first angle : "))
b = int(input("Second angle : "))
c = int(input("Third angle : "))


if a + b + c == 180:
  print("valid triangle")
else:
  print("invalid angle values added")