import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
browser.get('https://flight.naver.com/flights/')

# 가는 날 클릭
browser.find_element_by_link_text('가는날 선택').click()
browser.find_elements_by_link_text('24')[0].click()

# 오는 날 클릭
browser.find_elements_by_link_text('5')[1].click()

# 제주도 클릭
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]/div/span').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 로딩 중 다음 이미지 넘어가서 에러 발생
# -> sleep으로 해결하기에는 컴퓨터마다 sleep 환경 다름
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    print(elem.text)
except:
    print('실패했어요')

# 첫 번째 결과 출력(실패 경우)
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)

time.sleep(2)
browser.quit()
