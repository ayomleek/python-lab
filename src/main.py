from utils import square, is_even, celsius_to_fahrenheit, greet

name = input("Enter your name: ")
print(greet(name))

number = float(input("Enter a number: "))

print(f"The square of {number} is {square(number)}.")

if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print(f"{number}°C is equal to {celsius_to_fahrenheit(number)}°F.")