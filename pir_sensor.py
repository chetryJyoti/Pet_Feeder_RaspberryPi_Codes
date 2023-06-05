import RPi.GPIO as GPIO
import time

sensor_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

def detect_motion():
    print('ir sensor ready...')
    if GPIO.input(sensor_pin):
        print(GPIO.input(sensor_pin))
        print("Motion Detected")
        while GPIO.input(sensor_pin):
            time.sleep(.5)
            print('waiting for a while...')

        return True
    else:
        print("just waiting for a detection...")
        time.sleep(0.2)
        return False


# if __name__ == "__main__":


#     while True:
#         detect_motion()









