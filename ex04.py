# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве

print('Введите координаты точки 1')
x1 = int(input('Введите координату X1: '))
y1 = int(input('Введите координату Y1: '))

print('Введите координаты точки 2')
x2 = int(input('Введите координату X2: '))
y2 = int(input('Введите координату Y2: '))

distance=float(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
print('Расстояние между точками = {}'.format(round(distance,2)))