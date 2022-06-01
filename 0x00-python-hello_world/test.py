#!/usr/bin/python3
# Ask the uer to input 2 values and store them in num1 and num2
num1, num2 = input("Enter 2 numbers: ").split()
# Convert the strings into regular numbers Integer
num1 = int(num1)
num2 = int(num2)

# Add the value entered and store in sum
sum = num1 + num2
# Substract values and store them in difference
defference = num1 - num2
# Multiply the values and store them in product
product = num1 * num2
# Divide the values and store them in quotient
quotient = num1 / num2
# Use modulus on the values to find the remainder
remainder = num1 % num2
# Print the results
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {defference}")
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")
print(f"{num1} % {num2} = {remainder}")
