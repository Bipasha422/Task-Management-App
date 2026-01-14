rows = 3
cos = 3
for i in range(rows):
    for j in range(cos):
        if i == 0 or i == 2:
            print('*',end='')
        elif i == 1:
            if j == 0 or j == 2:
                print('*',end=" ")
            else:
                print(' ',end=" ")
                print()
            