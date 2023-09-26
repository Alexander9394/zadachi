a = int(input('Введите 1-е число: '))
b = int(input('Введите 2-е число: '))

if a % b == 0:
        print(a,'Делится',b)
     
else:
        print('Не делится')
        print( "Остаток деления: ", a % b)