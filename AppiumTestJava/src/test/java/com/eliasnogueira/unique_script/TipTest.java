package com.eliasnogueira.unique_script;

import static org.junit.Assert.*;

import java.net.MalformedURLException;
import java.net.URL;
import java.time.Duration;

import com.eliasnogueira.po.TestFlutterPageObject;
import io.appium.java_client.AppiumBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.AutomationName;
import io.appium.java_client.remote.MobilePlatform;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.eliasnogueira.support.Utils;

import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class TipTest {

	private AppiumDriver driver;
	
	@Before
	public void setUp() throws Exception {
//		driver = Utils.returnDriver(Utils.readProperty("run.platform"));
		DesiredCapabilities capabilities = new DesiredCapabilities();
		capabilities.setCapability("appPackage", "com.example.test_flutter");
		capabilities.setCapability("appActivity", ".MainActivity");
		capabilities.setCapability("automationName", AutomationName.ANDROID_UIAUTOMATOR2);
		capabilities.setCapability("deviceName", Utils.readProperty("device.android.name"));
		capabilities.setCapability("platformName", MobilePlatform.ANDROID);
		capabilities.setCapability("platform", MobilePlatform.ANDROID);
		capabilities.setCapability("noReset", "true");
		driver = new AndroidDriver(new URL("http://localhost:4723/wd/hub"), capabilities);
	}
	
//	@After
//	public void tearDown() {
//		driver.quit();
//	}
	
	@Test
	public void testCalculateDefaultTip() {
		TestFlutterPageObject testFlutter = new TestFlutterPageObject(driver);

		System.out.println("kyk / " + testFlutter.getTodoList());

		WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));
		wait.until(ExpectedConditions.elementToBeClickable(driver.findElement(AppiumBy.accessibilityId(testFlutter.getTodoList())))).click();

//		WebDriverWait wait2 = new WebDriverWait(driver, Duration.ofSeconds(20));
//		wait2.until(ExpectedConditions.elementToBeClickable(driver.findElement(AppiumBy.accessibilityId("2 / 27 / true / veritatis pariatur delectus")))).click();





//		MainScreenPageObject mainScreen = new MainScreenPageObject(driver);
//
//		mainScreen.fillBillAmount("100");
//		mainScreen.clickCalculateTip();
//
//		assertEquals("$15.00", mainScreen.getTipAmount());
//		assertEquals("$115.00", mainScreen.getTotalAmount());
		
	}

}
