# Import necessary modules
import time
from machine import Pin
from neopixel import Neopixel
from stockAPI import get_stock_change

# Neopixel setup
num_leds = 30
state_machine_id = 0  # Adjust based on your hardware setup
data_pin = Pin(28)  # Adjust based on your hardware setup
neopixel = Neopixel(num_leds, state_machine_id, data_pin, "GRB")


def display_percentage_difference(neopixel, percentage_diff):

    # Round to two decimal places
    rounded_percentage = round(percentage_diff, 2)

    # Determine color (red for negative, green for positive)
    rgb_color = (255, 0, 0) if rounded_percentage < 0 else (0, 255, 0)

    # Convert to string, handling negative percentages
    percentage_str = str(abs(rounded_percentage))

    # Check if the percentage is less than 1 and adjust the string to ensure it starts with "0."
    if rounded_percentage < 1:
        # Display "0." directly here before proceeding to the digits
        display_pair(neopixel, '0', '.', rgb_color, True)  # Initial display for "0."

    # Split the percentage string on the decimal point to handle digits after it
    if '.' in percentage_str:
        decimal_parts = percentage_str.split('.')
        if len(decimal_parts[1]) == 1:  # If there's only one digit after the decimal
            decimal_parts[1] += '0'  # Pad with zero to ensure two digits after the decimal
        left_digit, right_digit = decimal_parts[1][:2]  # Take the first two digits after the decimal
        display_pair(neopixel, left_digit, right_digit, rgb_color, False)  # Display subsequent digits


def display_pair(neopixel, left_digit, right_digit, rgb_color, initial_display=False):
        # Define the custom layout of LEDs for each digit
    digit_layout = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],  # 0
            [1, 2, 11, 12],  # 1
            [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15],  # 2
            [1, 2, 3, 4, 9, 10, 11, 12, 13, 14, 15],  # 3
            [1, 2, 5, 6, 11, 12, 13, 14, 15],  # 4
            [3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15],  # 5
            [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],  # 6
            [1, 2, 3, 4, 11, 12],  # 7
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],  # 8
            [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]   # 9
    ]
    # Display the left digit or "0."
    if left_digit == '0' and right_digit == '.':
        for segment in digit_layout[0]:  # Display "0" on left so add 14 to segment
            neopixel.set_pixel(segment + 14, rgb_color)
        neopixel.set_pixel(9, rgb_color)  # Display "." which is led #10
    else:
        neopixel.fill((0, 0, 0))
        for segment in digit_layout[int(left_digit)]:  # Display left digit
            neopixel.set_pixel(segment + 14, rgb_color) # Assuming 15 LEDs offset for the first digit
        for segment in digit_layout[int(right_digit)]:  # Display right digit with offset
            neopixel.set_pixel(segment - 1, rgb_color)  

    neopixel.show()
    time.sleep(1.5)  # Adjust timing as needed



