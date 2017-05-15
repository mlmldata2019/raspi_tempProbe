import RPi.GPIO as GPIO
import time

pin = 11 # This is the number of the GPIO pin the led should be connected to (GPIO17)
GPIO.setmode(GPIO.BOARD) #This tells the pi to use the pin numbers instead of the names
GPIO.setup(pin, GPIO.OUT)

led = GPIO.PWM(pin,200) # PWM stands for Pulse Width Modulation
led.start(0) # Initializes the LED at 0% duty cycle (off)

def toggle_on():
    # Turns on the LED
    led.ChangeDutyCycle(100)
    print('ON')

def toggle_off():
    # Turns off the LED
    led.ChangeDutyCycle(0)
    print('OFF')

def dot():
    '''
    Write a function that creates a dot in morse code with the LED
    You can use the time.sleep() function to pause your code for a number of seconds
    or a fraction of seconds
    '''

def dash():
    '''
    Write a function that creates a dash in morse code with the LED
    Hint, is three times as long as a dot
    '''

def MLML():
    '''
    write a function that when called, will signal MLML in Morse Code using
    the dot and dash functions you made before.
    Reference the Morse Code handout to 
    '''

if __name__ == "__main__":

    """ Use the space below to call the functions that you created above """

    # example code - toggle LED on for four seconds)
    toggle_on()
    time.sleep(4)
    toggle_off()

    # exit cleanly
    led.stop()
    GPIO.cleanup()
