print("Library Book Collection System")

book = input("Enter book name: ")
author = input("Enter author name: ")
copies = int(input("Enter number of copies: "))

print("\n--- Book Details ---")
print("Book Name:", book)
print("Author:", author)
print("Number of Copies:", copies)

if copies > 0:
    print("Status: Available")
else:
    print("Status: Not Available")