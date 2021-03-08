python = "Python is Amazing"

# 소문자
print(python.lower())

# 대문자
print(python.upper())

# 대문자인가?(boolean)
print(python[0].isupper())
# 문자 길이
print(len(python))
# 글자 대체
print(python.replace("Python", "Java"))

# n이 있는 index 위치
index = python.index("n")
print(index)

# 찾은 위치 이후 부터 두번째 n을 찾음
index = python.index("n", index + 1)
print(index)

# 글자 찾기, 없으면 -1
print(python.find("Java"))

# 반복
print('a의 2번 반복 : ',(a + ' ') * 2)