from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

# frame 전환
browser.switch_to_frame('iframeResult')

# cars에 해당하는 elememt를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# element = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')

# 텍스트 값을 통해서 선택하는 방법
# element = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# 텍스트 값이 특정 부분만 일치하는 것 선택
element = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Au")]')

element.click()

# browser.quit()