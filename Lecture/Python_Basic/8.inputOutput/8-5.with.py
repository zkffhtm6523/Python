# with

import pickle

with open("./Lecture/Python_Basic/8.inputOutput/profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

# 열었던 file을 close할 필요가 없음

# 파일 작성
with open("./Lecture/Python_Basic/8.inputOutput/study.txt","w",encoding="UTF8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
# 파일 읽기
with open("./Lecture/Python_Basic/8.inputOutput/study.txt","r",encoding="UTF8") as study_file:
    print(study_file.read())