import smtplib
from account import EMAIL_ADDRESS
from account import EMAIL_PASSWORD
from email.message import EmailMessage

msg = EmailMessage()
# 제목
msg["Subject"] = "테스트 메일입니다."
# 보내는 사람
msg["From"] = EMAIL_ADDRESS
# 받는 사람
msg["TO"] = "zkffhtm6523@gmail.com"
# 본문
msg.set_content("다운로드 하세요.")

# 파일 첨부
# Image[JPG]
# with open("myw3schoolsimage.jpg", "rb") as f:
#     msg.add_attachment(f.read(), maintype="image", subtype="jpg", filename=f.name)

# PDF
# with open("테스트.pdf", "rb") as f:
#     msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

# Excel
with open("enum.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)


# 기본값 : maintype="application", subtype="octet-stream"


# Google에서 MIME 타입 검색하기
# https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types


with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)