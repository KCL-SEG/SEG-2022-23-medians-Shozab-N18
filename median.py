"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
print(numbers)

first_num = 1
last_num = len(numbers)

while first_num < last_num:
    first_num = first_num + 1
    last_num = last_num - 1

if first_num == last_num:
    print(str(numbers[first_num-1]))
else:
    print(str((numbers[first_num-1] + numbers[last_num-1]) / 2))
