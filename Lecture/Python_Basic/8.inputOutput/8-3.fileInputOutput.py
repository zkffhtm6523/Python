# 파일 입출력
# 파일 열기, 없으면 새로 만들고 열기
score_file = open("./Lecture/Python_Basic/8.inputOutput/score.txt", "w", encoding="utf8")
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)

score_file.close()
# 두 번째 옵션 append
score_file = open("./Lecture/Python_Basic/8.inputOutput/score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽어오기
score_file = open("./Lecture/Python_Basic/8.inputOutput/score.txt", "r", encoding="utf8")
print(score_file.read())

score_file = open("./Lecture/Python_Basic/8.inputOutput/score.txt", "r", encoding="utf8")
print("--------------------------")
while True:
    line = score_file.readline()
    if not line:
        break   
    print(line)
score_file.close()


# list 형태로 저장
print("--------------------------")
score_file = open("./Lecture/Python_Basic/8.inputOutput/score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

score_file.close()