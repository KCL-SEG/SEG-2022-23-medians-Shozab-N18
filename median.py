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
        
first_num = numbers[0]
last_num = numbers[len(numbers) - 1]

while first_num < last_num:
    first_num = first_num +1
    last_num = last_num +1

if first_num == last_num:
    print(str(first_num))
else:
    print(str((first_num + last_num) / 2))

print(numbers)
