from neopixel import Neopixel

# Function to convert a temperature value to RGB color
def temperature_to_color(temperature):
    if temperature >= 40:
        return 255, 0, 0
    elif temperature <= -40:
        return 0, 0, 255
    elif temperature > 0:
        return 255, int(155 / temperature), int(155 / temperature)
    elif temperature < 0:
        return int(-155 / temperature), int(-155 / temperature), 255
    else:
        return 255, 255, 255  # White for 0

# Function to display a temperature value on the custom 7-segment display
def display_temperature(neopixel, temperature):
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

    # Convert the temperature to RGB color
    rgb_color = temperature_to_color(temperature)

    # Display digits on both sides
    for i in range(15):
        neopixel.set_pixel(i, rgb_color if i + 1 in digit_layout[abs(int(temperature)) % 10] else (0, 0, 0))

    for i in range(15, 30):
        neopixel.set_pixel(i, rgb_color if i + 1 - 15 in digit_layout[abs(int(temperature)) // 10] else (0, 0, 0))

    neopixel.show()

