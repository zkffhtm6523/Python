# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

name = "마린"
hp = 40
damage = 5

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")

# 탱크 : 공격 유닛, 포를 쏠 수 있는데, 일반 모드/시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
