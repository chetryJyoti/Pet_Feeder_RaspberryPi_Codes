# Pet Feeder RaspberryPi Codes (go to master branch)

This repository contains the necessary code to build an automated pet feeder system using Raspberry Pi. The code enables automatic feeding of pets based on various triggers and conditions.

## Repository Structure

- ***main.py***: This module serves as the main code controlling the overall functionality of the pet feeder system. It integrates different components such as servo motors, PIR motion sensors, and image capturing/uploading.

- ***servo_motor.py***: This module handles the control of the servo motor used in the pet feeder. It provides functions to open and close the feeder door based on specified angles.

- ***pir_sensor.py***: This module deals with the PIR motion sensor functionality. It contains code to initialize and read data from the PIR sensor, detecting motion in the vicinity of the pet feeder.

- ***capture_and_upload.py***: This module is responsible for capturing images using a connected camera and uploading them to a designated storage location, in this case a appwrite storage bucket.

- ***secretKeys.py***: This file stores sensitive information such as API keys or endpoints. It should not be shared publicly and should be kept secure.

The code makes use of external libraries and APIs, such as RPi.GPIO for GPIO control, requests for making HTTP requests, and Appwrite for interacting with the Appwrite backend service.

Overall, the Pet_Feeder_RaspberryPi_Codes repository provides a comprehensive set of code to implement an automated pet feeder system using Raspberry Pi, enabling convenient and controlled feeding of pets.


## *For the frontend codes of the app go to this link:*
[PetFeeder App](https://github.com/chetryJyoti/PetFeeder_IoT_app)


### More docs comming soon on how to use ....


