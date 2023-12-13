appium_server_host = 'http://localhost'
# appium_server_port = '4723'
# appium_server_base_path = '/wd/hub'
# def appium_server_url():
  # return f'{appium_server_host}:{appium_server_default_port}{appium_server_base_path}'
  # return f'{appium_server_host}:{appium_server_port}'

# 테스트할 디바이스
# 테스트 파이썬 스크립트 실행 시 전달받도록 함
device = 'aos_galaxy_note_10_plus'

capabilities = {
  "aos_galaxy_note_10_plus" : {
    "platformName": "Android",
    "appium:deviceName": "aos_galaxy_note_10_plus",
    "appium:udid": "R3CMA0F73PL",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.example.test_flutter",
    "appium:appActivity": ".MainActivity",
    "appium:autoGrantPermissions": "true",
    "appium:noReset": "true"
  },
  "aos_lg_q_51" : {
    "platformName": "Android",
    "appium:deviceName": "aos_lg_q_51",
    "appium:udid": "LMQ510NKFSO5L9SBAL",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.example.test_flutter",
    "appium:appActivity": ".MainActivity",
    "appium:autoGrantPermissions": "true",
    "appium:noReset": "true"
  },
  "aos_galaxy_s_20_5g" : {
    "platformName": "Android",
    "appium:deviceName": "aos_galaxy_s_20_5g",
    "appium:udid": "R3CN30JZ89F",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.example.test_flutter",
    "appium:appActivity": ".MainActivity",
    "appium:autoGrantPermissions": "true",
    "appium:noReset": "true"
  },
  "aos_galaxy_s_22_ultra" : {
    "platformName": "Android",
    "appium:deviceName": "aos_galaxy_s_22_ultra",
    "appium:udid": "R3CT10E16RK",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.example.test_flutter",
    "appium:appActivity": ".MainActivity",
    "appium:autoGrantPermissions": "true",
    "appium:noReset": "true"
  },
  "ios_iphone_se_2022" : {
    "platformName": "iOS",
    "appium:deviceName": "ios_iphone_se_2022",
    "appium:platformVersion": "15.4",
    "appium:udid": "00008110-00167D812280401E",
    "appium:automationName": "XCUITest",
    "appium:bundleId": "com.kykdev.testFlutter",
    "appium:xcodeOrgId": "kwon0koang@naver.com",
    "appium:xcodeSigningId": "iPhone Developer",
    "appium:autoGrantPermissions": "true",
    "appium:noReset": "true"
  },
}
ports = {
  "aos_galaxy_note_10_plus" : 4723,
  "aos_lg_q_51" : 4724,
  "aos_galaxy_s_20_5g" : 4725,
  "aos_galaxy_s_22_ultra" : 4726,
  "ios_iphone_se_2022" : 4727,
}








# AOS
# capabilities = {
#   "platformName": "Android",
#   "appium:deviceName": "Galaxy",
#   "appium:appPackage": "com.example.test_flutter",
#   "appium:appActivity": ".MainActivity",
#   "appium:automationName": "UiAutomator2",
#   "appium:autoGrantPermissions": "true",
#   "appium:noReset": "true"
# }

# todo kyk IOS
# capabilities = {
#   "platformName": "iOS",
#   "appium:platformVersion": "15.4",
#   "appium:deviceName": "iPhone SE",
#   "appium:udid": "00008110-00167D812280401E",
#   "appium:bundleId": "com.kykdev.testFlutter",
#   "appium:xcodeOrgId": "kwon0koang@naver.com",
#   "appium:xcodeSigningId": "Apple Developer",
#   "appium:automationName": "XCUITest",
#   "appium:autoGrantPermissions": "true",
#   "appium:noReset": "true",
# }
# todo kyk iOS 테스트 앱 성공
# capabilities = {
#   "platformName": "iOS",
#   "appium:deviceName": "iPhone SE",
#   "appium:platformVersion": "15.4",
#   "appium:automationName": "XCUITest",
#   "appium:udid": "00008110-00167D812280401E",
#   "appium:bundleId": "com.kykdev.IntegrationApp",
#   "appium:xcodeOrgId": "kwon0koang@naver.com",
#   "appium:xcodeSigningId": "iPhone Developer"
# }





# Temp
# "appium:udid": "auto",
# "appium:app": "com.kykdev.testFlutter",
# "appium:appName": "com.kykdev.testFlutter",
# "appium:allowProvisioningDeviceRegistration": "true",
# "appium:usePrebuildWDA": "true"

# iOS Success (https://velog.io/@tkjung/Appium-iOS-%ED%99%98%EA%B2%BD-%EC%85%8B%ED%8C%85#xcode%EC%97%90%EC%84%9C-webdriveragent-signing--build-settings-%EC%84%A4%EC%A0%95)
# 실물 기기
# {
#   "platformName": "iOS",
#   "appium:deviceName": "iPhoneX",
#   "appium:platformVersion": "15.2.1", 
#   "appium:automationName": "XCUITest",
#   "appium:udid": "{UDID}",
#   "appium:bundleId": "{실행할 앱의 Bundle ID}",
#   "appium:xcodeOrgId": "{애플 개발자 계정에서 식별해둔 Team ID}",
#   "appium:xcodeSigningId": "iPhone Developer"
# }
# 시뮬레이터
# {
#   "platformName": "iOS",
#   "appium:automationName": "XCUITest",
#   "appium:deviceName": "simulator",
#   "appium:platformVersion": "14.1",
#   "appium:udid": "{UDID}",
#   "appium:bundleId": "{실행할 앱의 Bundle ID}"
# }