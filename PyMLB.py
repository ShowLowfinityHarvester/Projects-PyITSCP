# These are school projects! Github page may be all cluttered until 2025 or 2026.

import math
while True:
    try:
        inp1 = int(input("Enter a number -> "))
        break
    except ValueError:
        print("Invald number")
x = math.pow(inp1, 3)
print(int(x))