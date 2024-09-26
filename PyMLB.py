import math
while True:
    try:
        inp1 = int(input("Enter a number -> "))
        break
    except ValueError:
        print("Invald number")
x = math.pow(inp1, 3)
print(int(x))