import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import subprocess
import re
import config

# config.py capabilities 에서 기기명 출력
def get_device_names(capabilities):
    device_names = []

    for device_key, device_info in capabilities.items():
        device_names.append(device_info["appium:deviceName"])

    return device_names

if __name__ == "__main__":
    device_names = get_device_names(config.capabilities)
    # print(device_names)
    for name in device_names:
        print(name)
