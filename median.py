"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        numbers_length = len(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

if(numbers_length % 2 == 0):
    print((numbers[int(numbers_length/2)] + numbers[int(numbers_length/2 - 1)]) / 2)
else:
    print(numbers[int(numbers_length/2)])
