import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# 파일로 저장
# img.save("screenshot.png")

# pyautogui.mouseInfo()

pixel = pyautogui.pixel(28, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(28, 18, (34, 167, 242)))
print(pyautogui.pixelMatchesColor(28, 18, pixel))