#!/usr/bin/env python3

message = 'Storm Classigfication: '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("What is the wind speed in MPH? "))

# check input and print corresponding category 
if connection >= 157:
    message = message + 'Category 5 hurricane'
elif connection >= 130:
    message = message + 'Category 4 hurricane'
elif connection >= 111:
    message = message + 'Category 3 hurricane'
elif connection >= 96:
    message = message + 'Category 2 hurricane'
elif connection >= 74:
    message = message + 'Category 1 hurricane'
elif connection >= 39:
    message = message + 'Tropical storm'
else:
    message = message + 'Tropical depression'
print(message)

