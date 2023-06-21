"""
Fill in the blanks to complete the “car_listing” function. 
This function accepts a “car_prices” dictionary. 
It should iterate through the keys (car models) and values (car prices) in that dictionary. 
For each item pair, the function should format a string so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". 
Each new string should appear on its own line.
"""

def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for car_prices, car_listing in car_prices.items():
    result += "{} costs {} dollars".format(car_prices, car_listing) + "\n" 
    # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars