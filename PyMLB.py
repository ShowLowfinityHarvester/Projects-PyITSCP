import math
while True:
    try:
        inp1 = int(input("Enter a number -> "))
        break
    except ValueError:
        print("Invald number")

while True:
    try:
        inp2 = int(input("Enter a number -> "))
        break
    except ValueError:
        print("Invald number")
bikes = inp1 / inp2
x = math.ceil(bikes)
print(f"In this town, for every bike that exists there are {x} people.")