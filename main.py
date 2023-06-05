from secret_keys import THINGSPEAK_CHANNEL_ID, THINGSPEAK_READ_API_KEY
from capture_and_upload import capture_and_upload_image
from pir_sensor import detect_motion
from servo_motor import handleServo
import time
import RPi.GPIO as GPIO
import requests
print("------Main code running-----")
GPIO.setmode(GPIO.BCM)

servo_state_handler_url = f'https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds/last.json?api_key={THINGSPEAK_READ_API_KEY}'


# currently facing problem of functions below running before above

def main():
    try:
        while True:
            response = requests.get(servo_state_handler_url)
            data = response.json()

            servo_control_data = None
            if 'field1' in data:
                servo_control_data = int(data['field1'])

            # Set the servo state based on the servo control value
            print("servo_control_data:",servo_control_data)
            if servo_control_data == 1:
                # api calls
                print('api calls...')
                print('feeding your pet...')
                handle_servo_motion()
                handle_servo_motion()
                time.sleep(.5)
                # capture_and_upload_image()
                print('capturing image....')
                time.sleep(6)
                continue

            # calling the pir_sensor to detect object
            if detect_motion():
                print('motion detected...')
                print('feeding your pet....')
                handle_servo_motion()
                handle_servo_motion()
                time.sleep(.3)
                print('capturing image....')
                # capture_and_upload_image()
                time.sleep(6)
                continue
            else:
                print("no motion")

    except KeyboardInterrupt:
        GPIO.cleanup()


def handle_servo_motion():
    handleServo("open")
    # print("feed on")
    handleServo("close")
    # print('off')


if __name__ == "__main__":
    GPIO.setwarnings(False)
    handleServo('close')
    main()
