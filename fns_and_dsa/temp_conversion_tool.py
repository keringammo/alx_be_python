# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter the temperature to convert: ").strip()
        try:
            temp = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Ask user for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
