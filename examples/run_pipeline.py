from src.capture_pipeline import capture_screen

device_id = "DEVICE_ID"
platform = "android"

endpoint = "AZURE_ENDPOINT"
api_key = "AZURE_KEY"

text = capture_screen(device_id, platform, endpoint, api_key)

print(text)