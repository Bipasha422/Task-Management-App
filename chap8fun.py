
def greatest(a,b,c):

    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
a=3
b=6
c=7
print(greatest(a,b,c))