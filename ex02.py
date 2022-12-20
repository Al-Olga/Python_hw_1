# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))

if x>0 and y>0:
    print('точка лежит в I четверти')
elif x<0 and y>0:
    print('точка лежит во II четверти')
elif x<0 and y<0:
    print('точка лежит в III четверти') 
elif x>0 and y<0:
    print('точка лежит в IV четверти') 
elif x==0 and y!=0:
    print('точка лежит на оси X')
elif x!=0 and y==0:
    print('точка лежит на оси Y')
else:
    print('точка соответствует 0')