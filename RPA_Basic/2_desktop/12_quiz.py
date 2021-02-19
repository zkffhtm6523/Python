# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오

# 1. 그림판 실행(단축키 : win + r, 입력값 : mspaint) 및 최대화

# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
# - 입력 글자 : "참 잘했어요"

# 3. 5초 대기 후 그림판 종료
# 이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyperclip
import sys
import pyautogui
# Test

# pyautogui.hotkey("win","r")
# pyautogui.write("notepad")
# pyautogui.press("enter")
# pyautogui.write("Hi~")

# 1번 완료
pyautogui.hotkey("win","r") # 단축키 : win + r
pyautogui.write("mspaint")
pyautogui.press("enter")

# 그림판 나타날 때까지 대기
pyautogui.sleep(2)
# 그림판 1개만 띄워져 있다고 가정
window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]   

if window.isMaximized == False:
    window.maximize() # 최대화

# 2번 완료
btn_text = pyautogui.locateOnScreen("rpa_basic/2_image/btn_text.png")
if btn_text:
    pyautogui.click(btn_text)
else:
    print("찾기 실패")
    sys.exit()

# 흰 영역 클릭
pyautogui.click(200, 200, duration=0.5)


def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(0.5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n")