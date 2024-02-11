menu = ["americano", "cookie", "latte", "brownie", "toastie"] # creating a list of items

# creating a dictionary with a key and value i.e. the item and the amount of that item in stock
stock = {'americano': 10,
 'cookie': 10,
 'latte': 10,
'brownie': 10,
'toastie': 10}

# creating another dictionary with a key and value i.e. the item and its price 
price = {'americano': 5,
'cookie': 5,
'latte': 5,
'brownie': 5,
'toastie': 5}

# work out the total value of stock in the cafe. 

""" get the the item from menu and its associated stock value and price. 
mulitply the stock item value by the price.
sum all the items to get the total stock value
loop through the menu to get its stock value and its price.
multiply the stock value of each item by its associated price"""

total_stock = 0 # stores the total stock value. starting it with 0 

for item in menu: # iterates through the list 
    total_stock += stock[item] * price[item] # for each item in the list, it adds the stock amount and the associated price
    print(f"{item}: {stock[item]} * {price[item]}") # using f string for readability

print("Total Stock Value: " + "£" + str(total_stock))





