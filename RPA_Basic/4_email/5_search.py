from imap_tools import MailBox
from account import EMAIL_ADDRESS
from account import EMAIL_PASSWORD

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# MailBox 자원 사용 후 반납
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # 전체 메일 다 가져오기
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)',limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM zkffhtm6523@gmail.com)', limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자 포함 메일(전체_영어)
    # for msg in mailbox.fetch('(TEXT "test")', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자 포함 메일(제목_영어)
    # for msg in mailbox.fetch('(SUBJECT "test")', limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자 포함 메일(제목_한글 가능)
    # for msg in mailbox.fetch(limit=3, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)',limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 메일
    # for msg in mailbox.fetch('(SENTSINCE 22-Feb-2021)',limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 참고 : https://pypi.org/project/imap-tools/

    # 2가지 이상의 조건을 모두 만족하는 메일(AND)
    # for msg in mailbox.fetch('(SENTSINCE 22-Feb-2021 SUBJECT "test")',limit=3, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일(OR)
    for msg in mailbox.fetch('(OR ON 21-Feb-2021 SUBJECT "testx")',limit=3, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject))