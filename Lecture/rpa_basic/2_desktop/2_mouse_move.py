import pyautogui

# https://note.redgoose.me/article/2119/
# ctrl + F9

# 마우스 이동
# 지정한 위치로 마우스를 이동
# pyautogui.moveTo(100, 100)

# 0.25초 동안 마우스 커서 이동
# pyautogui.moveTo(100, 200,duration=5)

# 연속 마우스 이동
# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)

# 상대 좌표 이동(현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100, duration=0.25)
# 100, 100 기준으로 +100, +100 -> 200, 200
pyautogui.move(100, 100, duration=0.25)
pyautogui.move(100, 100, duration=0.25)

# 현재 나의 마우스 커서 위치
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)