#Count Odd Digits
n = int(input("kasgfisd : "))
count = 0
while n>0:
  num = n % 10
  if num % 2 != 0:
    count += 1 
  n //=10
print(count)