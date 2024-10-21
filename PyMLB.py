# These are school projects! Github page may be all cluttered until 2025 or 2026.

Pizza = int(input("# of pizza slices -> "))
People = int(input("# of People -> "))

try:
    print(Pizza / People)
except:
    print("Your code doesn't account for if a user tries to enter 0 people")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")