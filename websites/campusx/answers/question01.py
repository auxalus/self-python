#Given three ages, determine which is the oldest.

age_of_candidate1 = int(input('Enter age : '))
age_of_candidate2 = int(input('Enter age : '))
age_of_candidate3 = int(input('Enter age : '))

if age_of_candidate1<age_of_candidate2 and age_of_candidate1<age_of_candidate3:
  print('smallest candidate is 1')
elif age_of_candidate2<age_of_candidate3:
  print('smallest candidate is 2')
else:
  print('smallest candidate is 3')