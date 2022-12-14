# 멤버 변수
class Unit:
    def __init__(self, name, hp, damage) : 
        self.name = name # 멤버 변수 : 클래스 내에서 정의된 변수, 그 변수를 가지고 초기화를 하거나 활용 가능
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) 
marine2 = Unit("마린", 40, 5) 
tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)

wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) #멤버 변수에 접근 가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("뺴앗은 레이스",80,5)
wraith2.cloking = True # cloking 이라는 멤버 변수는 없는데, 현재 추가 할당
#객체에 추가로 변수에서 사용 가능

if wraith2.cloking == True :
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))