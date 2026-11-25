print("Data Conversion Utility")
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", f)

elif choice == 2:
    km = float(input("Enter distance in Kilometers: "))
    miles = km * 0.621371
    print("Distance in Miles:", miles)

elif choice == 3:
    kg = float(input("Enter weight in Kilograms: "))
    pounds = kg * 2.20462
    print("Weight in Pounds:", pounds)

else:
    print("Invalid choice")