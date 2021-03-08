# 지역변수 / 전역변수

gun = 10

# 경계근무
def checkpoint(soldiers):
    # 전역 공간에 있는 gun 사용
    global gun
    # gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
    return gun


print("전체 총 : {}".format(gun))
# checkpoint(2) # 경계 2명 나감
gun = checkpoint_ret(gun, 2)
# return 값이 없으면 none을 변수에 넣겠다는 의미
print("남은 총 : {}".format(gun))