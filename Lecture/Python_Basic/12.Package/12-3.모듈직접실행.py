# 모듈 파일에서 CTL + F9로 실행하느냐, 패키지를 import로 해서 실행할 것이냐
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

# 파일 경로 알아보기
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))