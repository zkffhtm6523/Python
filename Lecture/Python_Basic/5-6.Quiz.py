# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

# 조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가능
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# --- 당첨자 발표 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2 ,3, 4]
# --- 축하합니다 ---

from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
# 섞기
shuffle(lst)
print(lst)
# 뽑기
print(sample(lst, 1))

users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)

print(users)
shuffle(users)
print(users)

# 4명 중에서 1명은 치킨, 3명은 커리
winners = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("-- 축하합니다 --")