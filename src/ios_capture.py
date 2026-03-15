import subprocess

def capture_ios_screen(device_id, output_path):

    try:
        devices = subprocess.check_output(
            ["idevice_id", "-l"]
        ).decode()

        if device_id not in devices:
            raise RuntimeError("iOS device not found")

        subprocess.run(
            ["idevicescreenshot", output_path],
            check=True
        )

    except FileNotFoundError:
        raise RuntimeError("libimobiledevice tools not installed")

    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to capture iOS screen")