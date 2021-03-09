# pickle
import pickle
# wb : write binary(이진법)
profile_file = open("./Lecture/Python_Basic/8.inputOutput/profile.pickle","wb")
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)

# profile에 있는 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()

# rb : read binary(이진법)
profile_file = open("./Lecture/Python_Basic/8.inputOutput/profile.pickle","rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()