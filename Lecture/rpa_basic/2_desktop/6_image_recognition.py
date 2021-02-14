from PIL.ImageOps import grayscale
import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")

print(file_menu)
pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 파일 및 이미지에 대한 모든 정보를 가져온다
# 1개 이상일 수 있기 때문에 반복문
# 이미지와 비슷한 체크박스를 클릭하는 것
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# locateOnScreen은 1개만, 반복문 사용 못함
# locateAllOnScreen은 2개 이상, 반복문 사용 가능

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정
# 어느 범위 사이에서 찾아라, 범위 좁혀지면 빨라짐
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881 - 1488, 137))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정(정확도를 떨어뜨려서 인식률 상승)
# run_btn = pyautogui.locateOnScreen("run_btn.png")
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")

# while file_menu_notepad in None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기(TimeOut)
import time
import sys

# # 10초 대기
# timeout = 10
# # 시작 시간 설정
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad in None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     # 지정한 10초를 초과하면
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target in None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break

    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

# pyautogui.click(file_menu_notepad)
my_click("file_menu_notepad.png", 1)
#˝