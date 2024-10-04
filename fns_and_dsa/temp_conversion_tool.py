FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
FREEZING_POINT_FAHRENHEIT = 32

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
