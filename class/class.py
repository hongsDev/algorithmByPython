class Person:
    def __init__(self, name):
        self.name = name
        #print("hihi i am creator")

    def talk(self):
        print("저는 ", self.name, "입니다.")


person1 = Person("hongsub")
person1.talk()








