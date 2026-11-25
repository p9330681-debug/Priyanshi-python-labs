print("Inventory Control System")

item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

print("\n--- Inventory Details ---")
print("Item Name:", item)
print("Quantity:", quantity)
print("Price per item:", price)
print("Total Stock Value:", total)

if quantity < 5:
    print("Stock Status: Low Stock")
else:
    print("Stock Status: Available")