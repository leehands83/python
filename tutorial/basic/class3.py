class Parent:
    def sing(self):
        print("Sing a Song")

class LuckyChild(Parent):
    def dance(self):
        print("shuffle dance")

luckyboy = LuckyChild()
luckyboy.sing()
luckyboy.dance()