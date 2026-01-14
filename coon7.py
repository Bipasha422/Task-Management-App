marks1 = int(input("Enter Marks 1"))
marks2 = int(input("Enter Marks 2"))
marks3 = int(input("Enter Marks 3"))

totalp =(100*(marks1+marks2+marks3))/300 
if(totalp>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")
else:
    print("you failed,try again later")