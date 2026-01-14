a=int(input("enter  number"))
b=int(input("enter  number"))
c=int(input("enter  number"))
d=int(input("enter  number"))
if(a>=b and a>=c and a>=d):
    print("a is greater")
elif(b>=c and b>=d and b>=a) :
    print("b is greater") 
elif(c>=d and c>=a and c>=b) :
    print("c is greater")
else:
    print("d is greatest") 