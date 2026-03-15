import logging
import os
import tempfile

from src.android_capture import capture_android_screen
from src.ios_capture import capture_ios_screen
from src.ocr_pipeline import extract_text_from_image

logging.basicConfig(level=logging.INFO)

def capture_screen(device_id, platform, endpoint, api_key):

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    image_path = temp_file.name
    temp_file.close()

    try:

        if platform == "android":
            logging.info("Capturing Android screen")
            capture_android_screen(device_id, image_path)

        elif platform == "ios":
            logging.info("Capturing iOS screen")
            capture_ios_screen(device_id, image_path)

        else:
            raise ValueError("Unsupported platform")

        logging.info("Sending image to Azure OCR")

        text = extract_text_from_image(
            image_path,
            endpoint,
            api_key
        )

        return text

    finally:
        if os.path.exists(image_path):
            os.remove(image_path)