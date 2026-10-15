# Palindrome number 


n = int(input('faduhisfduidfau : '))
rev = 0
k = n
while n>0:
  num = n % 10
  rev = (rev*10) + num
  n = n //10
print(k==rev)