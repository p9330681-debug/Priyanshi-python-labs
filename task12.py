print("Document Analysis System")

text = input("Enter document text: ")

words = len(text.split())
characters = len(text)
lines = len(text.splitlines())
vowels = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels = vowels + 1

print("\n--- Document Analysis ---")
print("Total Words:", words)
print("Total Characters:", characters)
print("Total Lines:", lines)
print("Total Vowels:", vowels)