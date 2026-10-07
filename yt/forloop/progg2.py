# for 10k population increasing by 10% per year. WAP to find population at the end of each year in last 10 years


current_polulation = 10000

for i in range(0,10,-1):
  print(i,current_polulation)
  current_polulation = current_polulation - (10/100)* current_polulation


total = 0

for num in range(1,6):
  total +=num

print(total)

