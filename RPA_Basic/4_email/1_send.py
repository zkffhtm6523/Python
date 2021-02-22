import smtplib
from account import EMAIL_ADDRESS
from account import EMAIL_PASSWORD

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    # 연결 확인
    smtp.ehlo()
    # 모든 내용 암호화 전송
    smtp.starttls()
    # 로그인
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # 메일 제목
    subject = "test mail"
    # 메일 본문
    body = "mail body"

    msg = f"Subject: {subject}\n{body}"
    
    # 발신자, 수신자, 정해진 형식의 메세지
    smtp.sendmail(EMAIL_ADDRESS, "zkffhtm6523@gmail.com", msg)
