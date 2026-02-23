width = int(input('Enter your width: '))
height = int(input('Enter your height: '))
i = 1
while i <= height:
    if i == 1 or i == height:
        j = 1
        while j <= width:
            print('*', end='')
            j = j + 1
    else:
        print('*', end='')
        j = 1
        while j <= (width - 2):
            print(' ', end='')
            j = j + 1
        print('*', end='')
    print()
    i = i + 1
