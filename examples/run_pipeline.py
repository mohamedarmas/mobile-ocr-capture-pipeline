import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.capture_pipeline import capture_screen

device_id = "R9ZY90E05VY"
platform = "android"

endpoint = "AZURE_ENDPOINT"
api_key = "AZURE_KEY"

text = capture_screen(device_id, platform, endpoint, api_key)

print(text)