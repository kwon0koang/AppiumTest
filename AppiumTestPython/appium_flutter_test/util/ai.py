from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import webdriver
import util.util as util

# ===================================================================================================================================================================================================================================================================================================================================================================================================================
def beforeRefactoring(driver: webdriver.WebDriver):
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Test element 1")
    el.click()
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Test element 2")
    el.click()
    el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Test element 3")
    el.click()
    
    el = driver.find_element(by=AppiumBy.ID, value="Test element 4")
    el.click()
    el = driver.find_element(by=AppiumBy.ID, value="Test element 5")
    el.click()
    el = driver.find_element(by=AppiumBy.ID, value="Test element 6")
    el.click()

    el = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView111")
    el.click()
    el = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView222")
    el.click()
    el = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView333")
    el.click()

    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText111")
    el.click()
    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText222")
    el.click()
    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText333")
    el.click()

    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText777")
    el.click()
    el.send_keys("aaa")
    driver.press_keycode(4, undefined, undefined);
    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText888")
    el.click()
    el.send_keys("bbb")
    driver.press_keycode(4, undefined, undefined);
    el = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText999")
    el.click()
    el.send_keys("ccc")
    driver.press_keycode(4, undefined, undefined);

# ===================================================================================================================================================================================================================================================================================================================================================================================================================
def afterRefactoring(self, driver: webdriver.WebDriver):
    id_test_element_1 = util.get_value(aos="Test element 1", ios="")
    util.click(self.driver, AppiumBy.ACCESSIBILITY_ID, id_test_element_1)
    id_test_element_2 = util.get_value(aos="Test element 2", ios="")
    util.click(self.driver, AppiumBy.ACCESSIBILITY_ID, id_test_element_2)
    id_test_element_3 = util.get_value(aos="Test element 3", ios="")
    util.click(self.driver, AppiumBy.ACCESSIBILITY_ID, id_test_element_3)
    
    id_test_element_1 = util.get_value(aos="Test element 1", ios="")
    util.click(self.driver, AppiumBy.ID, id_test_element_1)
    id_test_element_2 = util.get_value(aos="Test element 2", ios="")
    util.click(self.driver, AppiumBy.ID, id_test_element_2)
    id_test_element_3 = util.get_value(aos="Test element 3", ios="")
    util.click(self.driver, AppiumBy.ID, id_test_element_3)
    
    xpath_test_element_1 = util.get_value(aos="//android.widget.TextView111", ios="")
    util.click(self.driver, AppiumBy.XPATH, id_test_element_1)
    xpath_test_element_2 = util.get_value(aos="//android.widget.TextView222", ios="")
    util.click(self.driver, AppiumBy.XPATH, id_test_element_2)
    xpath_test_element_3 = util.get_value(aos="//android.widget.TextView333", ios="")
    util.click(self.driver, AppiumBy.XPATH, id_test_element_3)

    xpath_edit_text_1 = util.get_value(aos="//android.widget.EditText111", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_1)
    xpath_edit_text_2 = util.get_value(aos="//android.widget.EditText222", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_2)
    xpath_edit_text_3 = util.get_value(aos="//android.widget.EditText333", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_3)

    xpath_edit_text_777 = util.get_value(aos="//android.widget.EditText777", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_777)
    util.send_keys(self.driver, AppiumBy.XPATH, xpath_edit_text_777, "aaa")
    self.driver.hide_keyboard()
    xpath_edit_text_888 = util.get_value(aos="//android.widget.EditText888", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_888)
    util.send_keys(self.driver, AppiumBy.XPATH, xpath_edit_text_888, "bbb")
    self.driver.hide_keyboard()
    xpath_edit_text_999 = util.get_value(aos="//android.widget.EditText999", ios="")
    util.click(self.driver, AppiumBy.XPATH, xpath_edit_text_999)
    util.send_keys(self.driver, AppiumBy.XPATH, xpath_edit_text_999, "ccc")
    self.driver.hide_keyboard()
  
# ===================================================================================================================================================================================================================================================================================================================================================================================================================

def asis(self, driver: webdriver.WebDriver):
    el13 = driver.find_element(by=AppiumBy.ID, value="plus.steps.sapp.dev:id/btn_custom_keypad_confirm")
    el13.click()

# ===================================================================================================================================================================================================================================================================================================================================================================================================================

# beforeRefactoring() 함수를 리팩토링하면 afterRefactoring() 함수야. 이 두 함수를 학습해서 asis() 함수를 리팩토링해줘. 조건은 아래와 같아
# 함수명은 tobe(). 다른 말 하지말고 tobe() 함수만 만들어줘
# element 변수명은 id 혹은 xpath로 시작하고, 각각의 element를 식별하기 쉽도록 네이밍되어야 함
# 클릭 함수는 click_element_by_xpath 혹은 click_element_by_id
# 키 입력 함수는 send_keys_element_by_xpath 혹은 send_keys_element_by_id
# 주석은 필요없어
