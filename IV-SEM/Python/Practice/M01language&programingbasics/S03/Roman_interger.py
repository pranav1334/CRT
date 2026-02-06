roman = input("Enter a Roman numeral: ").upper()
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
total = 0
perv = 0
for ch in reversed(roman):
    if values[ch]<perv:
        total -= values[ch]
    else:
        total +=values[ch]
        perv = values[ch]
print("integer values:", total)            