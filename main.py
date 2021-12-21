toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2,6,1,3,2,7,2]

#count the number of occurences of the number 2 in prices list and store in variable twoDollarSlices and print
twoDollarSlices = [x for x in prices if x == 2]
# the first x holds the value to be added to the list for that iteration while second x holds the value of prices for that iteration
# if the x in prices == 2 for that iteration then it will be appended to the list
print(twoDollarSlices)
print(len(twoDollarSlices))# prints the size of the twoDollarSlices list
numOfPizzas = len(toppings)
print('We sell',numOfPizzas,'different kinds of pizza!')

pizzasAndPrices = []# empty list that will hold lists that contain pizza price and the corresponding pizza type

for count, x in enumerate(toppings):
  added = [prices[count],toppings[count]]
  pizzasAndPrices.append(added)

print(pizzasAndPrices)

pizzasAndPrices.sort()
print(pizzasAndPrices)

cheapestPizza = pizzasAndPrices[0]
priciestPizza = pizzasAndPrices[numOfPizzas-1]

pizzasAndPrices.pop()
print(pizzasAndPrices)

pizzasAndPrices.append([2.5,'peppers'])
pizzasAndPrices.sort()
print(pizzasAndPrices)

threeCheapest = pizzasAndPrices[:3]
print(threeCheapest)