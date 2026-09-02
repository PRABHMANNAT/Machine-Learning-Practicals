"""Small practice script for the Python Basics notebooks.

Run with: python test.py
Change the values, predict the output, then run it again.
"""

name = "Maya"
age = 8
favorite_number = 7

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1}.")
print(f"Your number is {'even' if favorite_number % 2 == 0 else 'odd'}.")

if age < 13:
    print("You are learning the foundations of Python.")
else:
    print("You are ready for the next challenge.")
