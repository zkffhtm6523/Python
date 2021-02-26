jumin = "990120-1234567"

print("성별 : {}".format(jumin[7]))
# index : 0이상 2미만
print("연 : {}".format(jumin[0:2]))
print("월 : {}".format(jumin[2:4]))
print("일 : {}".format(jumin[4:6]))

# print("생년월일 : {}".format(jumin[0:6])) # 아래와 같음
print("생년월일 : {}".format(jumin[:6]))

# print("뒤 7자리 : {}".format(jumin[7:14])) # 아래와 같음
print("뒤 7자리 : {}".format(jumin[7:]))

# 맨뒤(-1)에서 7번째부터 끝까지(-1)
print("뒤 7자리(뒤부터) : {}".format(jumin[-7:]))