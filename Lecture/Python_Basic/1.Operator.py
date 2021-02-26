# 연산자
print(2**3) # 2^3=8
print(5%3) # 나머지 2
print(5//3) # 몫 1

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

#boolean
print(True)
print(False)

#comparison boolean
print('비교 연산자 : ',1 == 2)

#in
print('in의 활용 : ','world' in 'hello world')

#path
import os.path
print('path도 boolean 가능 : ',os.path.exists('boolean.py'))
print('path도 boolean 가능 : ',os.path.exists('boolean.py'))
print('path도 boolean 가능 : ',os.path.exists('boolean.py'))


# 숫자 처리 함수
# 절대값
print(abs(-5)) # 5
# 승수
print(pow(4, 2)) # 4^2 = 4*4 = 16
# 최대값
print(max(5, 12)) # 12
# 최소값
print(min(5, 12)) # 5
# 반올림
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
# 내림
print(floor(4.99)) # 4
# 올림
print(ceil(3.14)) # 4
# 제곱근
print(sqrt(16)) # 4



