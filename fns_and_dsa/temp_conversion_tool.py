# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    try:
        return (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def convert_to_fahrenheit(celsius):
    try:
        return float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

# User interaction
if __name__ == "__main__":
    temp = input("Enter the temperature: ")
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        if unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp} Celsius is {result:.1f} Fahrenheit")
        elif unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp} Fahrenheit is {result:.1f} Celsius")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(e)
