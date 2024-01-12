import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import subprocess
import re
import config

# config.py capabilities 에서 기기명 출력 (연결된 기기만)
def get_connected_devices():
    try:
        result = subprocess.check_output([f"{os.environ['ANDROID_HOME']}/platform-tools/adb", 'devices']).decode('utf-8')
        devices = re.findall(r'(\S+)\s+device\b', result)
        return devices
    except subprocess.CalledProcessError as e:
        print(f"adb devices error / {e}")
        return []

def get_device_names(capabilities):
    connected_devices = get_connected_devices()
    device_names = []

    for device_key, device_info in capabilities.items():
        udid = device_info.get("appium:udid", "")
        if udid in connected_devices:
            device_names.append(device_info["appium:deviceName"])

    return device_names

if __name__ == "__main__":
    device_names = get_device_names(config.capabilities)
    if device_names:
        # print(device_names)
        for name in device_names:
            print(name)
