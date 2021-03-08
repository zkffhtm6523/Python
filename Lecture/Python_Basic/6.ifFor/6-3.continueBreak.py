# continue

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음

for student in range(1, 11): # 1 ~ 10
    if student in absent:
        print("{}, 결석".format(student))
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {}는 교무실로 따라와".format(student))
        break
    print("{}, 책을 읽어봐".format(student))