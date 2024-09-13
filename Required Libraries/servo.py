from machine import Pin, PWM
import utime
class Servo:
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 - 2 # offset for correction
    __max_u16_duty = 7864 - 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

# Create an instance of the Servo class
my_servo = Servo(pin=0)  # Adjust the pin number as needed

def move_servo_if_in_range(input_number):
    """
    Moves the servo to 30 degrees if the input number is within a specified range.
    """
    if -100 <= input_number <= -20:
        target_angle = 90
    elif -20 < input_number <= 0:
        target_angle = 90
    elif 0 < input_number <= 15:
        target_angle = 90
    elif 15 < input_number <= 25:
        target_angle = 120
    elif 25 < input_number <= 100:
        target_angle = 150
    else:
        print("Input number is out of the specified ranges.")
        return
    my_servo.move(target_angle)
        
 

# Example usage
# Define the range
 # Assume this is the received arbitrary number

