# Read a first name and a last name from input.
# Create a username by joining the two names together in lowercase (no space between them).
# Print these two lines:
# Username: [username]
# Initials: [first letter of first name][first letter of last name] (in uppercase)



first_name = input("first name: ")
last_name = input("last name: ")

username = first_name + last_name

print("Username: " , username.lower())

initial = first_name[0] + last_name[0]

print("Initials: ", initial.upper())
