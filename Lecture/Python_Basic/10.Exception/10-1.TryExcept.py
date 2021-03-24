try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# 에러별 상황 처리

# 이상한 값이 들어갔을 때
except ValueError:
    print("에러가 발생했습니다")
# 0으로 나눴을 때
except ZeroDivisionError as err:
    print(err)
# 이외 모든 에러
except as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)
