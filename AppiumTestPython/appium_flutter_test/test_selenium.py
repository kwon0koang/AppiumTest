from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# 네이버 열기
driver.get("https://www.naver.com/")

time.sleep(3)

# "경제" 찾아보기
el = driver.find_element(By.LINK_TEXT, "경제")

# "경제" 속성 살펴보기
el.get_attribute("class")

# "경제" 클릭
el.click()

time.sleep(3)

# 애플 검색하기
el = driver.find_element(By.CLASS_NAME, "search_input")
el.send_keys("AAPL")
el.send_keys(Keys.ENTER)

time.sleep(3)




