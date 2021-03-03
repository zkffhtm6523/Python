
# Dictionary
# : arraylist의 get과 JSON 
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))

print(cabinet[100])

# 에러 터짐
# print(cabinet[5])

# None 출력
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

# 새로운 값 부여
cabinet["C-20"] = "조세호"
print(cabinet)

# 지우기
del cabinet[3]
print(cabinet)

# key 출력
print(cabinet.keys())

# value 출력
print(cabinet.values())

# key-value
print(cabinet.items())

# 전부 delete
cabinet.clear()
print(cabinet)