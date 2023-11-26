from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 네이버 키기
driver.get("https://www.naver.com/")

# "경제" 찾아보기
el = driver.find_element(By.LINK_TEXT, "경제")

# "경제" 속성 살펴보기
el.get_attribute("class")

# "경제" 클릭
el.click()

# 애플 검색하기
el = driver.find_element(By.CLASS_NAME, "search_input")
el.send_keys("AAPL")
el = driver.find_element(By.CLASS_NAME, "btn_search")
el.click()

time.sleep(5)