import requests
from servo_motor import handleServo
import RPi.GPIO as GPIO
import time
from pir_sensor import detect_motion
from capture_and_upload import capture_and_upload_image
from secret_keys import THINGSPEAK_CHANNEL_ID,THINGSPEAK_READ_API_KEY 


servo_state_handler_url = f'https://api.thingspeak.com/channels/{THINGSPEAK_CHANNEL_ID}/feeds/last.json?api_key={THINGSPEAK_READ_API_KEY}'


#currently facing problem of functions below running before above

def main():
    print("------Main code running-----")
    try:
        while True:
            response = requests.get(servo_state_handler_url)
            data = response.json()

            servo_control_data = None
            if 'field1' in data:
                servo_control_data = int(data['field1'])

            # Set the servo state based on the servo control value
            if servo_control_data == 1:
                # api calls
                print('api calls...')
                handle_servo_motion()

            # calling the pir_sensor to detect object
            if detect_motion():
                print('motion')
                handle_servo_motion()
                time.sleep(5)
                capture_and_upload_image()
                time.sleep(4)
            else:
                print("no motion")

    except KeyboardInterrupt:
        GPIO.cleanup()


def handle_servo_motion():
    print("on")
    handleServo("open")
    print('off')
    handleServo("close")


if __name__ == "__main__":
    GPIO.setwarnings(False)
    main()
