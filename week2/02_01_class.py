

class Person:
    def __init__(self, name_param): # 생성자 : 객체를 만들 때 사용되는 함수
        self.name = name_param
        print("hihi im creative", self.name)

    def talk(self):
        print("안녕하세요 저는 ", self.name, " 입니다.")



person_1 = Person("유재석")
person_1.talk()
person_2 = Person("박명수")
print(person_2.talk())
