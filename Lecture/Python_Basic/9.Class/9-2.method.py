# 일반 유닛
class Unit:
    # Python의 생성자
    # 객체가 생성될 때 시작된다.
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
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