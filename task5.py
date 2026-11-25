print("Engineering Calculation Tool")
print("1. Area of Rectangle")
print("2. Force")
print("3. Work Done")
print("4. Power")

choice = int(input("Enter your choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area =", area)

elif choice == 2:
    m = float(input("Enter mass: "))
    a = float(input("Enter acceleration: "))
    force = m * a
    print("Force =", force, "N")

elif choice == 3:
    f = float(input("Enter force: "))
    d = float(input("Enter distance: "))
    work = f * d
    print("Work =", work, "J")

elif choice == 4:
    w = float(input("Enter work: "))
    t = float(input("Enter time: "))
    power = w / t
    print("Power =", power, "W")

else:
    print("Invalid choice")