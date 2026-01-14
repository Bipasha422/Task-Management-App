class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print("Brand title:",self.brand) 
        print ("color:",self.color)
        
b1=  car("python","pink") 
b1.start()
