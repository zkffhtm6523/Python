# 텍스트 파일에 이름 정보 넣는등 파일을 관리할 일 발생

# 파일 기본
import os
# current working directory 현재 작업 공간
# print(os.getcwd())
# # 작업 경로 변경
# os.chdir("rpa_basic")
# print(os.getcwd())

# # 부모 폴더 이동
# os.chdir("..")
# print(os.getcwd())

# # 조부모 폴더 이동
# os.chdir("../..")
# print(os.getcwd())

# # 절대 경로로 이동
# os.chdir("c:/")
# print(os.getcwd())

# 파일 경로 만들기
# 절대 경로 생성
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# os.path.dirname(r"D:\2_Develop\Python\Lecture\my_file.txt")

# 파일 정보 가져오기
import time
import datetime

file_path = "rpa_basic/2_desktop/11_file_system.py"

# 파일의 생성 날짜
ctime = os.path.getctime(file_path)
print(ctime)
print(datetime.datetime.fromtimestamp(ctime))
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일의 수정 날짜
mtime = os.path.getmtime(file_path)
print(mtime)
print(datetime.datetime.fromtimestamp(mtime))
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일의 마지막 접근 날짜
atime = os.path.getatime(file_path)
print(atime)
print(datetime.datetime.fromtimestamp(atime))
print(datetime.datetime.fromtimestamp(atime).strftime("%Y-%m-%d %H:%M:%S"))

# 파일 크기
size = os.path.getsize(file_path)
print(size)

# 파일 목록 가져오기
# print(os.listdir())
print(os.listdir("rpa_basic"))

# 파일 목록 가져오기(하위 폴더 모두 포함)
# 주어진 폴더 밑에 모든 폴더, 파일 목록 가져오기
# result = os.walk("rpa_basic")
# print(result)

# print("-------------------------")
# for root, dirs, files in result:
#     print(root, dirs, files)

# 응용) 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# .py로 끝나는 모든 파일
# pattern = "*.png"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root, name))
# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))

# 지정된 경로에 해당하는 파일 / 폴더가 없다면
# print(os.path.isfile("run_btn.png"))

# 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# 빈 파일 생성
# open("new_file.txt","a").close() 

# 파일명 변경하기
#  

# 파일 삭제
# os.remove("new_file.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준
# os.mkdir("D:/2_Develop/Python/Lecture/new_folder") # 절대 경로 기준

# 폴더 여러개 만들기(하위 경로)
# os.makedirs("new_folders/a/b/c")

# 폴더 지우기
# os.rmdir("new_folder")

#shell utilities
import shutil
# 폴더 안이 비어 있지 않아도 완전 삭제 가능
# shutil.rmtree("new_folders")