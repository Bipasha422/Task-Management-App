class Grand:
    def gr(self):
        print("i am grand")
class Parent(Grand):
    def par(self):
        print("i am parent")
class Child(Parent):
    def chi(self):
        print("i am child")
        c=Child()
        c.gr()
        c.par()
        c.chi()
        
        