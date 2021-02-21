import time
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
# 현재 윈도우 핸들 정보
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)
    # 각 핸들로 이동
    browser.switch_to_window(handle)

    # 출력해보면 현재 핸들(브라우저)의 제목 표시
    print(browser.title)

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행
print('현재 핸들 닫기')
browser.close()

# 이전 핸들로 돌아오기
print('처음 핸들로 돌아오기')
browser.switch_to_window(curr_handle)

# 브라우저 컨트롤 가능한지 확인
time.sleep(2)
browser.get('http://daum.net')

# HTML input type="radio"
print(browser.title)

time.sleep(2)
browser.quit()