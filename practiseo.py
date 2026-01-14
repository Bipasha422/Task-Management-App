class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name= name
        self.salary= salary
        self.pin=pin
        
p= Programmer("harry",12000,245001)
print(p.name,p.salary,p.pin,p.company)
r=Programmer("bipasha",20000,346789)
print(r.name,r.salary,r.pin)       
        