# 다중 상속 : 부모 여러명

# pass : 생성자 초기화 시 넣어줄 코드가 없을 때 pass 넣어줌
        # 즉, 해당 부분에서 오류가 발생하지 않도록 코드가 없음을 선언해주는 것
        # pass

# 일반 유닛(부모 클래스)
class Unit:
    # Python의 생성자
    # 객체가 생성될 때 시작된다.
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

# 공격 유닛(자식 클래스)
# Java : extends ~~~ / Python : (~~~)
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        # 상속 방법
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # self로 현재 class의 변수를 가져올 수 있음
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격[공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {self.damage}")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp}입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공격유닛 + 드랍쉽
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    # Unit(부모 클래스의 메소드 재정의)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # super로 초기화 시 self는 필요 없음
        super().__init__(name, hp, 0)
        self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     # pass

game_start()
game_over()