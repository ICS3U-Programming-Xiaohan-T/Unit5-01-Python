#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 5, 2025
# This program converts celsius to fahrenheit.


def farenheit():
    # This function gets the celsius from the user and converts it to fahrenheit
    celcius_str = input("Enter a temperature in Celsius: ")

    try:
        # Convert the user input into a float
        celsius = float(celcius_str)

        # Call the conversion function
        fahrenheit = celsius * 9 / 5 + 32

        # Display the result
        print(
            "{0} degrees Celsius is equal to {1} degrees Fahrenheit.".format(
                celsius, fahrenheit
            )
        )

    except Exception:
        # If the input can't be converted to float, show error
        print("Invalid input. Please enter a number.")
    # This function converts celsius to fahrenheit


def main():
    # This function gets the celsius from the user and converts it to fahrenheit
    farenheit()


if __name__ == "__main__":
    main()
