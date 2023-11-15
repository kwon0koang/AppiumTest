
appium_server_url = 'http://localhost:4723/wd/hub'

aos_capabilities = {
  "platformName": "android",
  "appium:deviceName": "galaxy",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.example.test_flutter",
  "appium:appActivity": ".MainActivity",
  "appium:autoGrantPermissions": True,
  "appium:noReset": True
}
ios_bundle_id = "com.kykdev.testFlutter"
ios_capabilities = {
  "platformName": "ios",
  "appium:deviceName": "iphone se",
  "appium:platformVersion": "15.4",
  "appium:udid": "00008110-00167D812280401E",
  "appium:automationName": "xcuitest",
  "appium:bundleId": ios_bundle_id,
  "appium:xcodeOrgId": "kwon0koang@naver.com",
  "appium:xcodeSigningId": "iPhone Developer",
  "appium:autoGrantPermissions": True,
  "appium:noReset": True
}


# AOS
# capabilities = {
#   "platformName": "Android",
#   "appium:deviceName": "Galaxy",
#   "appium:appPackage": "com.example.test_flutter",
#   "appium:appActivity": ".MainActivity",
#   "appium:automationName": "UIAutomator2",
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
#   "platformName": "ios",
#   "appium:deviceName": "iPhone SE",
#   "appium:platformVersion": "15.4",
#   "appium:automationName": "xcuitest",
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
#   "platformName": "ios",
#   "appium:deviceName": "iPhoneX",
#   "appium:platformVersion": "15.2.1", 
#   "appium:automationName": "xcuitest",
#   "appium:udid": "{UDID}",
#   "appium:bundleId": "{실행할 앱의 Bundle ID}",
#   "appium:xcodeOrgId": "{애플 개발자 계정에서 식별해둔 Team ID}",
#   "appium:xcodeSigningId": "iPhone Developer"
# }
# 시뮬레이터
# {
#   "platformName": "ios",
#   "appium:automationName": "xcuitest",
#   "appium:deviceName": "simulator",
#   "appium:platformVersion": "14.1",
#   "appium:udid": "{UDID}",
#   "appium:bundleId": "{실행할 앱의 Bundle ID}"
# }