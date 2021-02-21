import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[10]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# time.sleep(2)
# browser.quit()

# 방법 2 : 좌표 정보 이용
# 함수 아님, () 쓰지마세요
# xy = elem.location_once_scrolled_into_view
# print("type : ", type(xy)) # dict
# print("value : ", xy)

elem.click()

time.sleep(2)
browser.quit()