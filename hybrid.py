class A:
    def Displin(self):
        print("class A")
class B(A):
    def Displi(self):
        print("class B") 
class C:
    def Displ(self):
        print("class c")
class D(B,C):
    def Disp(self):
        print("class D")
obj=D()
obj.Displin() 
obj.Displi()
obj.Displ()
obj.Disp()