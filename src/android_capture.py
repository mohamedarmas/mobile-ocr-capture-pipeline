import subprocess
import shutil

def capture_android_screen(device_id, output_path):

    if not shutil.which("adb"):
        raise RuntimeError("ADB is not installed or not in PATH")

    command = [
        "adb",
        "-s",
        device_id,
        "exec-out",
        "screencap",
        "-p"
    ]

    try:
        with open(output_path, "wb") as f:
            subprocess.run(command, stdout=f, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Failed to capture Android screen") from e