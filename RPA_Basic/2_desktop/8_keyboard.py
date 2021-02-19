# 맥북 적용 안 됨;;

# table 20-1에 키보드 명령어 나와있음

# https://automatetheboringstuff.com/2e/chapter20/

import pyautogui

# 메모장 1개 띄운 상태에서 가져옴
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# 한글은 안 됨;
pyautogui.write("12345")
pyautogui.write("NadoCoding", interval=1)

# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, l a 순서대로 적고 enter
pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)

# shift를 누른 상태에서
pyautogui.keyDown("shift")
# 숫자 4를 입력하고
pyautogui.press("4")
# shift 키를 뗀다
pyautogui.keyUp("shift")

# 조합키(Hot Key) - 복잡하다
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")

# 간편한 조합키 - 간편하다
pyautogui.hotkey("ctrl", "alt", "shift", "a")
# Ctrl -> Alt -> Shift -> A -> A 떼고 -> Shift 떼고 -> Alt 떼고

# 한글 처리
# pip install pyperclip

import pyperclip
# "나도코딩" 글자를 클립보드에 저장
# pyperclip.copy("나도코딩")

# 클립보드에 있는 내용을 붙여넣기
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# win : ctrl + alt + del
# mac : cmd + shift + option + q