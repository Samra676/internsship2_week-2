#Create a temperature converter:
#Ask the user to input temperature in Celsius.
#Convert it to Fahrenheit using: F = (C*9/5) +32, Then reverse: Ask for Fahrenheit, convert it to Celsius.

# Celsius to Fahrenheit
celsius = float(input("Please enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")

# Fahrenheit to Celsius
fahrenheit_input = float(input("\nNow enter the temperature in Fahrenheit: "))
celsius_converted = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input:.2f}°F is equal to {celsius_converted:.2f}°C")
