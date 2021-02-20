# 1. pip install selenium 설치
# 2. 브라우저를 컨트롤할 수 있는 드라이버 설치
# : chrome://version 버전과 맞는 드라이버 설치
# $ xattr -d com.apple.quarantine chromedriver
# : 권한부여


from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
# 현재 폴더 기준
# browser = webdriver.chrome()

# browser.get("https://naver.com")

# elem = browser.find_element_by_link_text("카페")
# # 태그 안에 '카페'라는 Text가 있는 태그 찾기

# print(elem.get_attribute("href"))
# # # 그 태그의 href 가져오기
# print(elem.get_attribute("class"))


# elem.click() # 해당 엘리멘트 클릭
# browser.back() # 브라우저 뒤로 가기
# browser.forward() # 브라우저 앞으로 가기
# browser.refresh() # 새로 고침
# browser.back() # 브라우저 뒤로 가기

# elem = browser.find_element_by_id("query")
# elem.send_keys("나도코딩")

# 엔터 치기 위해서 Import
from selenium.webdriver.common.keys import Keys
# elem.send_keys(Keys.ENTER)

# elem = browser.find_element_by_tag_name("a")
# print(elem.get_attribute("href"))

# elems = browser.find_elements_by_tag_name("a")

# for e in elems:
#     print(e.get_attribute("href"))

browser.get("https://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()
browser.save_screenshot("3_web/daum.png")

# browser.quit()
browser.close()