appium_server_url = 'http://localhost:4723/wd/hub'

capabilities = {
  "platformName": "Android",
  "appium:deviceName": "R3CMA0F73PL",
  "appium:appPackage": "com.example.test_flutter",
  "appium:appActivity": ".MainActivity",
  "appium:automationName": "UIAutomator2",
  "appium:autoGrantPermissions": "true", # 권한 자동 허용
  "appium:noReset": "true" # 앱 재설치 X
}