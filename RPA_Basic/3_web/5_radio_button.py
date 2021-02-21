from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

# frame 전환
browser.switch_to_frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="male"]')

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택 안 됨, 선택하기")
    elem.click()
else: #라디오 선택이 되어 있으면
    print("선택되어 있음")

time.sleep(2)

browser.quit()