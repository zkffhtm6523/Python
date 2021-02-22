import time

# 현재 날짜를 요일-일-월-연도
print(time.strftime('%a-%d-%b-%Y'))

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime("%d-%b-%Y"))