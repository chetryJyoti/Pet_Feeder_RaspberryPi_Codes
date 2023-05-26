import RPi.GPIO as GPIO
import time

sensor_pin = 36
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)
print("Initializing PIR Sensor...")
time.sleep(12)
print("PIR Ready...")

def detect_motion():

    if GPIO.input(sensor_pin):
        # print(GPIO.input(sensor_pin))
        # print("Motion Detected")
        return True
    else:
        # print("just chilling...")
        time.sleep(0.2)
        return False


if __name__ == "__main__":


    motion_detected = detect_motion()









