import pyautogui

# 3초 대기
# pyautogui.sleep(3)
# print(pyautogui.position())

# 좌표를 마우스로 클릭 1초 동안 이동 후
# pyautogui.click(64, 17, duration=1)

# pyautogui.mouseDown()
# pyautogui.mouseUp()

# 더블 클릭
# pyautogui.doubleClick()

# 500번 클릭
# pyautogui.click(clicks=500)

# pyautogui.moveTo(100, 100)
# 마우스 버튼 누른 상태
# pyautogui.mouseDown()
# pyautogui.moveTo(200, 300)
# 마우스 버튼 뗀 상태
# pyautogui.mouseUp()

# 마우스 우클릭
# pyautogui.rightClick()

# 마우스 휠 클릭
# pyautogui.middleClick()

# 현재 위치 기준으로 x 100만큼 y 0 만큼 드래그
# pyautogui.moveTo(1114, 349)
# 상대좌표로 드래그
# pyautogui.drag(100, 0, duration=2)

# 절대좌표로 드래그
# pyautogui.dragTo(1514, 349, duration=2)

# 양수이면 위 방향으로, 300만큼 스크롤
pyautogui.scroll(-1000)