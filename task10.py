print("Text Processing Tool")

text = input("Enter any text: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Total characters:", len(text))
print("Total words:", len(text.split()))
print("Reversed text:", text[::-1])