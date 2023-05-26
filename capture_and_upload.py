from appwrite.client import Client
from appwrite.input_file import InputFile
from appwrite.services.storage import Storage
from picamera import PiCamera
import time
from secret_keys import APPWRITE_ENDPOINT, APPWRITE_PROJECT_ID, APPWRITE_API_KEY, APPWRITE_BUCKET_ID


def capture_and_upload_image():
    # Initialize the Appwrite client
    client = Client()
    client.set_endpoint(APPWRITE_ENDPOINT)
    client.set_project(APPWRITE_PROJECT_ID)
    client.set_key(APPWRITE_API_KEY)

    storage = Storage(client)

    
    camera = PiCamera()
    camera.start_preview()
    time.sleep(5)

    # Generate a unique file name using a timestamp
    # timestamp = int(time.time())
    # print(timestamp)
    file_name = time.strftime("%Y-%m-%d_%H-%M-%S") + '.jpg'
    # print(file_name)
    image_path = '/home/pi/Desktop/Codes/petFeederApp/images/' + file_name

    camera.capture(image_path)
    camera.stop_preview()
    camera.close()


    try:
        # Upload the image file
        response = storage.create_file(
            APPWRITE_BUCKET_ID ,
            file_name,
            InputFile.from_path(image_path),
        )

        print('Image uploaded successfully!')
        print('File ID:', response['$id'])

        return file_name  
    except Exception as e:
        print('Image upload failed:', str(e))

# print(capture_and_upload_image())
# print(time.strftime("%Y-%m-%d_%H-%M-%S"))