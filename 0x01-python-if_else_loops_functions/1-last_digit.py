#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Setting the number positive if necessary
if number >= 0:
    positive = number
else:
    positive = number * -1
# Use modulus on number and 10 to find the remainder
last_digit = positive % 10
if last_digit > 5:
    print(F"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(F"Last digit of {number} is {last_digit} and is 0")
else:
    print(F"Last digit of {number} is {last_digit} and is less than 6 and not 0")
    
