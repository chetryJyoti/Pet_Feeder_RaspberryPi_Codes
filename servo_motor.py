# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 37 as an output, and define as servo1 as PWM pin
GPIO.setup(37,GPIO.OUT)
servo1 = GPIO.PWM(37,50) # pin 37 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

angle1 = 0.0
angle2 = 80.0


def handleServo(status):
#this code just opens and closes the servo motor and waits for 5s delay as iam 
    if status == "open":
        print(2+(angle2/18))
        servo1.ChangeDutyCycle(2+(angle2/18))
        time.sleep(.5)
        servo1.ChangeDutyCycle(0)
        print(2+(angle1/18))
        servo1.ChangeDutyCycle(2+(angle1/18))
        time.sleep(5)

    elif status == "close":
        print(2+(angle1/18))
        servo1.ChangeDutyCycle(2+(angle1/18))

    time.sleep(.5)
    servo1.ChangeDutyCycle(0)
    


