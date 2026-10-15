#Digit in a number

n = int(input("kasgfisd : "))
count = 0
while n>0:
  count+=1
  n //=10

print(count)