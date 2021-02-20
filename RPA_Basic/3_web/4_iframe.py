from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver')

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

# iframe 태그의 name이나 id로 전환 필요
# 전환하지 않으면 xpath 찾지 못함
browser.switch_to_frame('iframeResult') # 프레임으로 들어가기

# 성공 예정

elem = browser.find_element_by_xpath('/html/body/form/label[1]')

elem.click()

browser.switch_to_default_content() # 상위로 빠져나옴

# 실패 예정

# elem = browser.find_element_by_xpath('/html/body/form/label[2]')

time.sleep(2) # 2초 대기

browser.quit()

