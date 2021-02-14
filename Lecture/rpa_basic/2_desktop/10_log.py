# 작업화를 실행하고 있을 떄는 print를 확인할 수 없기 때문에
# 로그를 작성한다

import logging

# level = debug 이상 level은 다 찍어준다, critical을 적을 시 낮은 레벨은 안 보여줌
# format %(asctime)s 시간 정보
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# debug < info < warning < error < critical 
logging.debug("아 이거 누가 짠거야~~~")
logging.info("자동화 수행 준비")
logging.warning("이 스크립트는 조금 오래 되었습니다. 실행 상에 문제가 있을 수 있습니다.")
logging.error("에러가 발생하였습니다. 에러 코드는....")
logging.critical("복구가 불가능한 심각한 문제가 발생했습니다.")

# 터미널과 파일에 함께 로그 남기기