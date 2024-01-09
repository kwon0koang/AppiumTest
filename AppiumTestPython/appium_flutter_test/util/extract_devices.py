import ast

def extract_devices(config_file_path):
    with open(config_file_path, 'r') as file:
        config_content = file.read()

    # 파이썬 코드로 읽어들임
    config_module = ast.parse(config_content)

    # 파싱된 모듈에서 기기 이름을 추출
    device_names = []
    for node in config_module.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            variable_name = node.targets[0].id
            if variable_name == 'capabilities':
                for key in node.value.keys:
                    if isinstance(key, ast.Str):
                        device_names.append(key.value)

    return device_names

if __name__ == '__main__':
    config_file_path = '/Users/kwon0koang/kykdev/0400_Appium/AppiumTest/AppiumTestPython/appium_flutter_test/config.py'  # 실제 파일 경로로 변경해야 함
    devices = extract_devices(config_file_path)
    # print(devices)
    print("[devices] ================================")
    for device in devices:
        print(device)
    print("==========================================")
