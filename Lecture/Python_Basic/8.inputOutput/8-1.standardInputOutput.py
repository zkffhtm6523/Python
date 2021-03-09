# 8-1 표준 입출력

import sys
print("Python", "Java", sep=", ", end="?")
# end = 개행 대신 무엇을 적을 것인가?
print("무엇이 더 재밌을까요?")

# log 출력할 때 표준 출력
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# dictionary(key, value)
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003
for num in range(1, 21):
    # zfill(3) : 3글자로 맞춤
    print("대기번호 : "+str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
# input은 return 타입 String
print("입력하신 값은 "+str(answer)+" 입니다.")