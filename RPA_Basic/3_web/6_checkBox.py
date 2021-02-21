from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

# frame 전환
browser.switch_to_frame('iframeResult')

element = browser.find_element_by_xpath('//*[@id="vehicle1"]')
element = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
element = browser.find_element(By.ID, 'vehicle1')

if element.is_selected() == False:
    print("선택해야됨")
    element.click()
else:
    print("선택되어 있음")

time.sleep(2)

browser.quit()