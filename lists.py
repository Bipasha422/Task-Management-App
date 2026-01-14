cuty=[10,20,4,45,99]
cuty=list(set(cuty))
cuty.sort()

print(cuty[-2])


mine = [1,2,3,3,4,4,5,6]
unique=[]
for item in mine:
    if item not in unique:
        unique.append(item)
        print(unique)

a = [1,2,3,4]
b = [3,4,5,6]
common = []
for item in a:
    if item in b and item in common:
        common.append(item)
        print(common)
   
  