# 다중 상속 : 부모 여러명

# 일반 유닛(부모 클래스)
class Unit:
    # Python의 생성자
    # 객체가 생성될 때 시작된다.
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛(자식 클래스)
# Java : extends ~~~ / Python : (~~~)
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        # 상속 방법
        Unit.__init__(self, name, hp)
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

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
            
# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공격유닛 + 드랍쉽
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")