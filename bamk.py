class Person:
    def __init__(self,name,age):
        self.__age = age
        self.name=name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("invalid age")       
p1 = Person("bipasha",19)
print("Name",p1.name)
print("age",p1.get_age())
p1.set_age(20)
print("updated age:",p1.get_age())