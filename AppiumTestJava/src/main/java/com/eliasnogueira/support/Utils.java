package com.eliasnogueira.support;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Properties;

import io.appium.java_client.remote.AutomationName;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebElement;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.remote.MobilePlatform;

public class Utils {

	public static String readProperty(String property) {
		Properties prop;
		String value = null;
		try {
			prop = new Properties();
			prop.load(new FileInputStream(new File("config.properties")));

			value = prop.getProperty(property);

			if (value == null || value.isEmpty()) {
				throw new Exception("Value not set or empty");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}

		return value;
	}


//	public static AppiumDriver<?> returnDriver(String platform) throws Exception {
//		AppiumDriver<?> driver;
//		DesiredCapabilities capabilities = new DesiredCapabilities();
//
//		if (Boolean.parseBoolean(Utils.readProperty("run.hybrid"))) {
//			capabilities.setCapability(MobileCapabilityType.AUTO_WEBVIEW, true);
//		}
//
//		String completeURL = "http://" + Utils.readProperty("run.ip") + ":" + Utils.readProperty("run.port") + "/wd/hub";
//
//		switch (platform.toLowerCase()) {
//
//		case "ios":
//			capabilities.setCapability(MobileCapabilityType.APP, new File(Utils.readProperty("app.ios.path")).getAbsolutePath());
//			capabilities.setCapability(MobileCapabilityType.DEVICE_NAME, Utils.readProperty("device.ios.name"));
//			capabilities.setCapability(MobileCapabilityType.PLATFORM_VERSION, Utils.readProperty("platform.ios.version"));
//			capabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.IOS);
//			capabilities.setCapability(MobileCapabilityType.PLATFORM, MobilePlatform.IOS);
//			capabilities.setCapability(MobileCapabilityType.NO_RESET, true);
//
//			if ( Boolean.parseBoolean(Utils.readProperty("platform.ios.xcode8"))) {
//				capabilities.setCapability(MobileCapabilityType.AUTOMATION_NAME, "XCUITest");
//			}
//
//			driver = new IOSDriver<RemoteWebElement>(new URL(completeURL), capabilities);
//			break;
//
//		case "android":
////			capabilities.setCapability(MobileCapabilityType.APP, new File(Utils.readProperty("app.android.path")).getAbsolutePath());
//			capabilities.setCapability("appPackage", "com.example.test_flutter");
//			capabilities.setCapability("appActivity", ".MainActivity");
//			capabilities.setCapability(MobileCapabilityType.AUTOMATION_NAME, AutomationName.ANDROID_UIAUTOMATOR2);
//			capabilities.setCapability(MobileCapabilityType.DEVICE_NAME, Utils.readProperty("device.android.name"));
//			capabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, MobilePlatform.ANDROID);
//			capabilities.setCapability(MobileCapabilityType.PLATFORM, MobilePlatform.ANDROID);
//			capabilities.setCapability(MobileCapabilityType.NO_RESET, true);
//
////			"platformName": "Android",
////				"appium:deviceName": "R3CMA0F73PL",
////				"appium:appPackage": "com.example.test_flutter",
////				"appium:appActivity": ".MainActivity",
////				"appium:automationName": "uiautomator2",
////				"appium:autoGrantPermissions": "true", # 권한 자동 허용
////			"appium:noReset": "true" # 앱 재설치 X
//
//			driver = new AndroidDriver<RemoteWebElement>(new URL(completeURL), capabilities);
//			break;
//
//		default:
//			throw new Exception("Platform not supported");
//		}
//
//		return driver;
//	}
}
