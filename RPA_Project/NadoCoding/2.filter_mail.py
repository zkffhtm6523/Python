import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Properties.account import EMAIL_ADDRESS
from Properties.account import EMAIL_PASSWORD
from imap_tools import MailBox

# 지원자 리스트
applicant_list = []

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 순번
    index = 1
    # 2021년 2월 25일 이후
    for msg in mailbox.fetch('(SENTSINCE 25-FEB-2021)'):
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} / 닉네임 : {} / 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

    for applicant in applicant_list:
        print(applicant)