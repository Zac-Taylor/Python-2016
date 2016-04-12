#Zachary Taylor IST 282
total_price = 0.0
ship_cost = 0.0
tax = .075
order_price = 0.0
num_book = 0

total_price = float(input("Enter the total book price:" + " "))
num_book = int(input("Enter the number of books:" + " "))

ship_cost = num_book * 2

tax = total_price * 0.075

order_price = total_price + ship_cost + tax

print("total cost of the order is$",order_price)
