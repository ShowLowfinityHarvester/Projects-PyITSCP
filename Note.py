# These are school projects! Github page may be all cluttered until 2025 or 2026.

# Python Math library basics

import math
x = math.ceil(2.8)
x = math.floor(7.2)
x = math.sqrt(4.5)
x = math.pow(6,5)

# Python Datetime

import datetime
x = datetime.datetime.now()
today = datetime.date.today()
print(x)
print(today)
print(x.strftime("%X"))
print(x.strftime("%m"))
print(x.strftime("%d"))
print(x.strftime("%Y"))

# Printing specifics in python

print("This is an example of a \n New Line")
print("This is an example of a \t New Tab")
print("This is an example of a \r Carriage return")

# Different Concatenating Approaches

name = "Doutree"
dogs = 3
location = "Albuquerque, New Mexico"

print("My name is " + name + "and I have "+ str(dogs) + " dogs and live in "+ location) # + approach
print(f"My name is {name} and I have {dogs} dogs and live in {location}") # F string approach
print("My name is", name, "and I have", dogs , "dogs and live in", location) # Comma approach
