print("----- SHOP BILLING SYSTEM -----")

item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total=price*quantity

print("\n----- BILL -----")
print("Item Name:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Total Bill:", total)
print("Thank you for shopping!")