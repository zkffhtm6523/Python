# 맥북은 지원 안 함;;

import pyautogui

# 현재 활성화된 창 (VSCode)
fw = pyautogui.getActiveWindow()

# 창의 제목
print(fw.title)

# 창의 크기
print(fw.size)

# 창의 좌표 정보
print(fw.left, fw.top, fw.right, fw.bottom)

pyautogui.click(fw.left + 25, fw.top + 20)

# 모든 윈도우 가져오기
# for i in pyautogui.getAllWindows():
#     print(i)

# 타이틀이 제목없는 것 중 첫 번째
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)

# 현재 활성화가 되지 않았다면
if w.isActive == False:
    # 활성화(맨 앞으로 가져오기)
    w.activate()

# 현재 최대화가 되지 않았다면
if w.isMaximized == False:
    # 최대화
    w.maximize()

# 현재 최소화가 되지 않았다면
if w.isMinimized == False:
    # 최소화
    w.minimize()

# 화면 원복
w.restore()

# 윈도우 닫기
w.close()