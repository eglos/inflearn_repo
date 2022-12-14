# __init__()
class Unit:
    def __init__(self, name, hp, damage) : # __init__() : 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # 클래스로부터 만들어 지는 것을 객체라고 하며, Unit 클래스의 인스턴스라고 한다.
marine2 = Unit("마린", 40, 5) # self를 제외하고 동일한 파라미터만큼 채워야 함.
tank = Unit("탱크", 150, 35)