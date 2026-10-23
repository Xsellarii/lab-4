text = input()

letters = sum(1 for char in text if char.isalpha())
digits = sum(1 for char in text if char.isdigit())

print(f"Letters {letters}")
print(f"Digits {digits}")