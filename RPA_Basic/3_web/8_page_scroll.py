from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.nhn')

# 무선마우스 입력
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')
# 검색 버튼 클릭 Enter 처리
elem.send_keys(Keys.ENTER)

# 스크롤
# 지정한 위치로 스크롤 내리기
# 모니터 해상도 높이 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, 1080)') # 1920 * 1080

# 화면 가장 아래로 스크롤(키보드 END 누르는 효과)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 반복 수행
# 2초에 한 번씩 스크롤 내리기
interval = 2 

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기(2초)
    time.sleep(2)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    # 직전 높이와 같으면, 높이 변화가 없으면
    if curr_height == prev_height:
        break

    prev_height = curr_height

browser.execute_script('window.scrollTo(0, 0)')
time.sleep(1)
browser.quit()