# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

week_day = int(input('Введите день недели (значение от 1 до 7): '))
if week_day == 6 or week_day == 7:
    print('введенное число соответсвует выходному дню')
else:
    if 0<week_day<6:
        print('введенное число соответсвует рабочему дню')
    else:
        print('введенное число не соответсвует дню недели')