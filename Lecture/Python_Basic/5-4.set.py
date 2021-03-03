# 집합(Set)
# 중복 X, 순서 X

my_set = {1, 2, 3, 4, 5}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java와 python 가능)
print(java & python)
print(java.intersection(python))

# 합집합(java or python)
print(java | python)
print(java.union(python))

# 차집합 (java는 가능, python은 불가능)
print(java - python)
print(java.difference(python))

# 집합 추가
python.add("김태호")
print(python)

# 집합 삭제
java.remove("김태호")
print(java)