# Stock and Weather Display with 7-Segment LEDs

## Overview
This project uses a two-digit 7-segment LED display to show real-time stock numbers and weather data. Powered by a Raspberry Pi Pico and programmed in MicroPython, it fetches data from external APIs and visualizes it on a 7-segment LED display. The project includes a servo motor that adjusts based on temperature data, and an LCD display for additional information.

## Features
- **Real-Time Data Display:** Shows stock percentage changes and current weather temperature on a 7-segment LED display.
- **Servo Control:** Adjusts a servo motor position based on temperature readings.
- **LCD Screen:** Provides additional data display and scrolling text of current stock or weather information.
- **Button Toggle:** Allows users to switch between stock and weather displays with a button press.

## Prerequisites
Before running the project, ensure you have the following:
- Raspberry Pi Pico
- MicroPython installed on the Pico
- Necessary libraries installed (`neopixel`, `machine`, `utime`, etc.)
- Internet connection for API data

## Hardware Setup
- **7-Segment Display:** 30 LEDs connected to GPIO pins via Neopixel.
- **Servo Motor:** Connected to GPIO pin 0.
- **LCD Display:** Connected via I2C with address `0x27`.
- **Button:** Connected to GPIO pin 14.

## Installation
1. **Clone or Download:** Clone this repository to your local machine.
2. **Connect Hardware:** Set up the 7-segment display, servo motor, LCD display, and button according to the hardware setup instructions.
3. **Upload Code:** Upload the `main.py` script to your Raspberry Pi Pico.

## Code Description
- **Imports:**
  - Libraries for handling LEDs, servo, I2C communication, and data retrieval.
- **Initialization:**
  - Set up Neopixel LEDs, LCD display, and button.
- **Functions:**
  - `show_stocks()`: Fetches and displays stock percentage changes.
  - `show_weather()`: Fetches and displays current temperature, controls the servo motor.
  - `toggle_display()`: Switches between stock and weather displays.
  - `debounce_button()`: Ensures reliable button presses.

## How to Run
1. Connect your Raspberry Pi Pico to your computer.
2. Ensure all hardware is connected properly.
3. Run the MicroPython script on your Raspberry Pi Pico:
   ```python
   python main.py
4. Press the button to toggle between stock and weather displays.

## Example Outputs
- **Stock Display:** Shows percentage change and scrolling stock information on the 7-segment LED display and updates the LCD with the latest stock data.
- **Weather Display:** Shows current temperature on the 7-segment LED display, updates the servo motor position based on temperature, and displays weather information on the LCD.

## Future Improvements
- Enhance API integration to provide more detailed stock and weather data.
- Implement more advanced servo control mechanisms based on additional environmental parameters.
- Add additional user interaction features, such as the ability to manually select different stock or weather metrics for display.

## License
This project is open-source and available under the [MIT License](LICENSE).
