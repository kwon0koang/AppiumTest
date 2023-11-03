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

import static java.time.Duration.ofSeconds;

public class TestFlutterPageObject {

//	@AndroidFindBy(id = "Todo list")
//	@iOSXCUITFindBy(xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]")
//	@FindBy(id = "billAmount")
//	public WebElement todoList;

	@AndroidFindBy(accessibility = "Todo list")
	@iOSXCUITFindBy(xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]")
	@FindBy(id = "todo")
	WebElement todoList;

	@AndroidFindBy(accessibility = "2 / 27 / true / veritatis pariatur delectu")
	@iOSXCUITFindBy(xpath = "//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]")
	@FindBy(id = "todo")
	WebElement todoItem;


	public TestFlutterPageObject(AppiumDriver driver) {
		PageFactory.initElements(new AppiumFieldDecorator(driver, ofSeconds(20)), this);
	}

	public String getTodoList() {
		return todoList.getTagName();
	}

	public String getTodoItem() {
		return todoItem.getTagName();
	}
}
