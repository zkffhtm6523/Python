# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

# 리스트 출력
subway = [subway1, subway2, subway3]
print(subway)

# subway2는 몇 번째 index에 있는가
print(subway.index(subway2))

# append
subway.append(40)
print(subway)

# list 사이에 삽입
subway.insert(2, 25)
print(subway)

# 뒤에서 한 개씩 꺼냄
print(subway.pop())
print(subway)

# 정방향
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 역방향
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)
