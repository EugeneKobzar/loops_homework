n = int(input('Enter the number in range from 5 to 15: '))
f = 1
if 4 < n < 16:
    for i in range(1, n + 1):
        f = f * i
    print('Factorial is equal to: ', f)
else:
    print("Invalid result")
