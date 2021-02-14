import pyautogui

# pyautogui.mouseInfo()
# 352,121 NA_on_macOS NA_on_macOS

# 모든 동작에 1초씩 sleep 적용
pyautogui.PAUSE = 1

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)
    
