import smtplib
from account import EMAIL_ADDRESS
from account import EMAIL_PASSWORD
from email.message import EmailMessage

# 이전 시간
# 발신자, 수신자, 정해진 형식의 메세지
# smtp.sendmail(EMAIL_ADDRESS, "zkffhtm6523@gmail.com", msg)

msg = EmailMessage()
# 제목
msg["Subject"] = "테스트 메일입니다."
# 보내는 사람
msg["From"] = EMAIL_ADDRESS
# 받는 사람
msg["TO"] = "zkffhtm6523@gmail.com"

# 여러 명에게 메일을 보낼 때
# 1번
# msg["TO"] = "zkffhtm6523@gmail.com, zkffhtm6523@naver.com"
# 2번
# to_list = ["zkffhtm6523@gmail.com, zkffhtm6523@naver.com"]
# msg["TO"] = ", ".join(to_list)

# 참조 메일 보내기
# msg["Cc"] = "zkffhtm6523@gmail.com"

# 비밀 참조
# msg["Bcc"] = "zkffhtm6523@gmail.com"

# 본문
msg.set_content("테스트 본문입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)