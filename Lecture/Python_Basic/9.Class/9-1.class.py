class Unit:
    # Python의 생성자
    # 객체가 생성될 때 시작된다.
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

# self를 제외한 나머지만 Parameter
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
marine3 = Unit("마린", 40, 5)

wraith1 = Unit("레이스", 80, 5)
# 멤버 변수를 외부에서 사용할 수 있음
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")