class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
    
class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() #앞에 있는 Flyable에 대한 생성자를 super로 인식


dropship = FlyableUnit()