# Task1
# n = int(input('Введите расстояние, которое авто проходит за день: '))
# m = int(input('Введите общий пробег: '))

# print(f"Потребуется {(m+n-1) // n} дней")


# Task2

# x = int(input('Введите кол-во учеников в первом классе'))
# y = int(input('Введите кол-во учеников во втором классе'))
# z = int(input('Введите кол-во учеников в третьем классе'))

# res = (x+1) // 2 + (y+1) // 2 + (z+1) // 2
# print(res)

# Task3

# i = int(input('Введите номер поезда от головы: '))
# j = int(input('Введите фактический номер поезда: '))

# if i!=j:
#     res = i + j - 1
# else:
#     res = 'Информации недостаточно'

# print(res)

# Task4

# year = int(intput('Введите год: '))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('Год високосный')
# else:
#     print('Год не високосный')

# Home_Task1

# x = int(input('Введите трехзначное число: '))

# if x >= 100 and x <=999:
#     a = x % 10
#     b = (x // 10) % 10
#     c = x // 100
#     print(a+b+c)
# else:
#     print('Некорректный ввод')

# Home_Task2

# S = int(input('Введите общее кол-во журавликов: '))

# if S % 6 == 0 and S != 0:
#     x = S//6
#     print(f'Катя сделала {x*4} журавликов, а Петя и Сережа по {x}')
# else: 
#     print('Такое невозможно')

# Home_Task3

# number = input('Введите шестизначный номер билета: ')
# if len(number) == 6:
#     sum1 = int(number[0]) + int(number[1]) + int(number[2])
#     sum2 = int(number[3]) + int(number[4]) + int(number[5])
#     if sum1 == sum2:
#         print('Поздравляем, у вас счастливый билет')
#     else:
#         print('Не сегодня')
# else:
#     print('Не правильный номер')

#Home_Task4

# m = int(input('Введите длину шоколадки: '))
# n = int(input('Введите ширину шоколадки: ')) 
# k = int(input('Введите сколько долек вы хотите отломить: '))

# if k<= m*n and k % m == 0 or k % n == 0:
#     print('Приятного аппетита')
# else:
#     print('Неее, не получится')