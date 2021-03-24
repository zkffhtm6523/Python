# 패키지 모음 사이트 : https://pypi.org/
# 웹스크래핑 : beautifulsoup(pip install beautifulsoup4)
# 버전 정보 확인 : pip show beautifulsoup4
# 버전 업그레이드 : pip install --upgrade beautifulsoup4
# 삭제 : pip un install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())