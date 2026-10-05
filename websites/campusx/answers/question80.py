
# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost_price = int(input("add costing price :"))
selling_price = int(input("add selling price :"))

if cost_price == selling_price:
  print("no profit no loss")
elif selling_price > cost_price:
  print("profited!")
elif cost_price > selling_price:
  print("loss")
else:
  print( "error")