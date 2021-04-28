class MyClass:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def method(self,str):
        print(self.id)
        print(self.name)
        print("method",str)
    def add(self,a,b):
        return a+b


obj = MyClass(1,'init')
str1 = "nhlee"
str2 = "yhkim"

obj.method(str1)
MyClass.method(obj,str1)
