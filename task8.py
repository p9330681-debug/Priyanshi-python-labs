print("School Result Processing System")

name = input("Enter student name: ")

m1 = int(input("Enter marks in English: "))
m2 = int(input("Enter marks in Maths: "))
m3 = int(input("Enter marks in Science: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")