# 클래스 바로 import 안됨
# import travel.thailand.ThailandPackage()
import travel.thailand

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()