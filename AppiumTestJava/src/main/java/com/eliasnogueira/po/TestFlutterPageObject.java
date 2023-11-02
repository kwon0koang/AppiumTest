package com.eliasnogueira.po;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.WithTimeout;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;
import java.time.temporal.ChronoUnit;
import java.util.concurrent.TimeUnit;

public class TestFlutterPageObject {

	@AndroidFindBy(id = "Todo list")
	@iOSXCUITFindBy(xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]")
	@FindBy(id = "billAmount")
	@WithTimeout(time = 10, chronoUnit = ChronoUnit.SECONDS)
    WebElement todoList;

//	@AndroidFindBy(id = "org.traeg.fastip:id/calcTipButton")
//	@iOSFindBy(xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[1]")
//	@FindBy(id = "calcTip")
//	MobileElement calculateTip;

	public TestFlutterPageObject(AppiumDriver driver) {
		AppiumFieldDecorator appiumFieldDecorator = new AppiumFieldDecorator(driver, Duration.ofSeconds(20));
		PageFactory.initElements(appiumFieldDecorator, this);
	}

	public String getTodoList() {
		return todoList.getText();
	}
}
