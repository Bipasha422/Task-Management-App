fruits = ['append','banana']
fruits.append('cherry')
fruits.insert(1,'alu')
veget=['carrot','ladies finger']
fruits.extend(veget)
fruits.remove('carrot')
fruits.pop(4)
print(fruits.index('cherry'))
print(fruits.count('alu'))
fruits.clear()
print(fruits)