a = list(map(int, input("Введите массив (целые числа через пробел): \n").split()))
print('Числа кратные 3-м:',end=' ')
for i in a:
    if not i%3:
        print(i,end=' ')
