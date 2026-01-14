from abc import ABC,abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth=breadth
    def area(self):
        return self.length+self.breadth
    def perimeter(self):
        return 2*(self.length*self.breadth)
length=float(input("Enter length of rectangle"))
breadth=float(input("Enter breadth of rectangle"))
rect=Rectangle(length, breadth)
print("Area of Rectangle:",rect.area())
print("perimeter of Rectangle:",rect.perimeter())

            