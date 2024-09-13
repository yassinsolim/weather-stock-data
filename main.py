import math
import time
import machine
from machine import Pin, I2C
from neopixel import Neopixel
from weatherAPI import weather_stats
from weather_led import display_temperature
from stockAPI import get_stock_change
from stock_led import display_percentage_difference
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from servo import move_servo_if_in_range
import utime
from servo import Servo
latest_temp = None 
my_servo = Servo(pin=0)

num_leds = 30  # 30 LEDs for the custom 7-segment display
state_machine_id = 0 
data_pin = 28 
neopixel = Neopixel(num_leds, state_machine_id, data_pin, "GRB")

neopixel.fill((0, 0, 0))
neopixel.show()

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = machine.Pin(2)
scl = machine.Pin(3) # NOTE: It is important you change this to match the SDA and SCL pins you are using.
i2c_controller = 1    # Also change this to match the controller you are using (Listed on the Raspberry Pi Pico W Pinout as "I2C0" or "I2C1")
                      

i2c = I2C(i2c_controller, sda=sda, scl=scl, freq=400000) 
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

current_time = machine.RTC().datetime()
formatted_date = "{:04d}-{:02d}-{:02d}".format(current_time[0], current_time[1], current_time[2])

# Global state to track the current display mode
current_mode = "stocks"  # Initial mode

def show_stocks():
    neopixel.fill((0, 0, 0))
    stock_url = "https://api.tiingo.com/tiingo/daily/AAPL/prices?token=9eb25974d78a1b0a4f7804d0aaeaa405e01c6ae0"
    percentage_change = get_stock_change(stock_url)["percent"]
    display_percentage_difference(neopixel, percentage_change)
    stock_stats = f"{formatted_date} {get_stock_change(stock_url)["data"]}"
    for i in range(len(stock_stats) - 15):
        lcd.putstr(stock_stats[i:i+16])
        time.sleep(0.35)
        lcd.move_to(0,0)

    
def show_weather():
    global latest_temp
    neopixel.fill((0, 0, 0))
    # Assuming weather_stats() is defined elsewhere and returns weather data including temperature
    temp = weather_stats()["temp"]
    temperature = round(temp[0])  # Assuming this gets the temperature in Celsius
    latest_temp = temperature
    display_temperature(neopixel, temperature)
    
    # Call the function to move the servo if temperature is between -10 and 0 degrees Celsius
      # Specify the correct GPIO pin number for the servo
    move_servo_if_in_range(temperature)
    
    weather_data = f"{formatted_date} Temp: {temperature}C"
    for i in range(len(weather_data) - 15):
        lcd.putstr(weather_data[i:i+16])
        utime.sleep(0.3)
        lcd.move_to(0,0)

def toggle_display():
    global current_mode
    if current_mode == "stocks":
        current_mode = "weather"
        if latest_temp is not None:  # Check if temperature is available
            # Use the latest temperature to move the servo
            my_servo.move(90)
        show_weather()
    else:
        current_mode = "stocks"
        my_servo.move(0)
        show_stocks()   


# Main loop
last_button_state = button.value()
while True:
    current_button_state = button.value()
    if current_button_state != last_button_state:  # Check for state change
        last_button_state = current_button_state  # Update the last state
        if current_button_state:  # If the button is pressed
            toggle_display()
            time.sleep(0.5)  # Debounce delay

def debounce_button(button):
    time.sleep(0.05)  # Short delay to debounce
    return button.value()

# Main loop
while True:
    if debounce_button(button) and not last_button_state:  # Button pressed
        last_button_state = True  # Update last button state to prevent multiple detections
        toggle_display()
    elif not button.value():
        last_button_state = False  # Reset last button state when button is released
    time.sleep(0.1)  # Small delay to reduce CPU usage
    
