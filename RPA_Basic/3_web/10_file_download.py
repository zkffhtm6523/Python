from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':'/Users/david/Programming/Python/RPA_Basic'})

browser = webdriver.Chrome('./chromedriver', options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to_frame('iframeResult')

# download 링크 클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(2)
browser.quit()