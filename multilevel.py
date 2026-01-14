class Father:
    def skills(self):
        print("Gardening,Programming")
class Mother:
    def hobbies(self) :
        print("cooking,painting")
class Child(Father,Mother) :
    def sports(self):
        print("post,good") 
c = Child() 
c.skills()
c.hobbies()
c.sports()                    