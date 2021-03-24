from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

# 정의되지 않았다고 함. 
# 패키지 안에 포함된 것 중에서 공개/비공개 선택 필요
# __init__.py에서 __all__ = ["vietnam"] 선언하면 *을 사용 가능