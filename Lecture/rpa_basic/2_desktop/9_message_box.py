import pyautogui

# print("곧 시작합니다...")
# pyautogui.countdown(3)
# print("자동화 시작")

# 확인 버튼만 있는 팝업
# pyautogui.alert("자동화 수행에 실패했습니다","경고")

# 확인, 취소 버튼
# result = pyautogui.confirm("계속 진행하시겠습니까?","확인")
# print(result)

# 사용자 입력
# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까","입력")
# print(result)

# 비밀번호 입력
result = pyautogui.password()
print(result)

