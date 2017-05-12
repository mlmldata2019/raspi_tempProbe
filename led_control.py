import RPi.GPIO as GPIO
import time

# Housekeeping
pin = 11 # This is the number of the GPIO pin the led should be connected to (GPIO17)
GPIO.setmode(GPIO.BOARD) #This tells the pi to use the pn numbers instead of the names
GPIO.setup(pin, GPIO.OUT)

led = GPIO.PWM(pin,200) # PWM stands for Pulse Width Modulation

def init_led():
    # Initializes the LED at a full duty cycle (100%)
    led.start(100)

def toggle_on():
    # Turns on the LED
    led.ChangeDutyCycle(100)
    print('ON')

def toggle_off():
    # Turns off the LED
    led.ChangeDutyCycle(0)
    print('OFF')


time_unit = .5

def dot()
    '''
    Write a function that creates a dot in morse code with the LED
    You can use the time.sleep() function to pause your code for a number of seconds
    or a fraction of seconds
    '''
    toggle_on()
    time.sleep(time_unit)
    toggle_off()
    

def dash()
    '''
    Write a function that creates a dash in morse code with the LED
    Hint, is three times as long as a dot
    '''
    toggle_on()
    time.sleep(time_unit)
    toggle_off()

def MLML()
    '''
    write a function that when called, will signal MLML in Morse Code using
    the dot and dash functions you made before.
    Reference the Morse Code handout to 
    '''

if __name__ == "__main__":
    init_led()
    # Write your some lo


    led.stop()
    GPIO.cleanup()
