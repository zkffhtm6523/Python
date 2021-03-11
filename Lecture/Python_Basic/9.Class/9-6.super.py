class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super를 썼을 시 Unit이 나옴
        # super().__init__()

        # -----------------------
        # 명시적으로 다중상속 시 이렇게 함
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽 = 다중상속 시 Unit의 생성자가 나옴 
dropship = FlyableUnit()