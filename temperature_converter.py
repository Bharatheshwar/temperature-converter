# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_other(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_other(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_other(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Main program
def convert_temperature():
    print("Temperature Conversion Tool")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")

    choice = int(input("Choose an option (1/2/3): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit, kelvin = celsius_to_other(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius, kelvin = fahrenheit_to_other(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C = {kelvin:.2f}K")

    elif choice == 3:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius, fahrenheit = kelvin_to_other(kelvin)
        print(f"{kelvin}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    convert_temperature()
