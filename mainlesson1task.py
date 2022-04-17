# Задание время в секундах
# вар1
sec = int(input("Введите кол-во секунд для конвертации в формате чч.мм.сс.:"))
print(f"{sec // 3600:.0f}:{(sec // 60) % 60:.0f}:{sec % 60:.0f}")
# Вар2
while True:
    number_seconds = input("Введи время в секундах: ")
    if number_seconds.isdigit():
        number_seconds = int(number_seconds)
        break
    print("Нужно ввести число")
print(f"{number_seconds // 3600:0{2}}:{(number_seconds) // 60:0{2}}:{(number_seconds % 3600) % 60:0{2}}")
# Вар3
sec = int(input("Введите время в секундах: "))
print(f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}")
# Вар4
import datetime
sec = int(input("enter number of seconds: "))
print(datetime.time(sec // 3600, (sec % 3600) // 60, (sec % 3600) % 60))

# Вар5
import time
sec_numb = int(input("enter number of seconds: "))
print(time.strftime('%H:%M:%S', time.gmtime(sec_numb)))

# Задание 3 Узнать у пользователя число n. Найти сумму чисел n+nn+nnn.
n = input('Enter a number: ')
while n < '0':
    print('The number should be greater than 0!!! Please try again.')
    n = input('Please enter a number greater than 0: ')
print(int(n) + int(n + n) + int(n + n + n))
# Вар
n = input("Enter a number: ")
print(int(n) + int(n * 2) + int(n * 3))
# Вар с форматированием
n = int(input('Enter a number, '))
set_1 = int("%d%d%d" % (n,n,n))
set_2 = int("%d%d" % (n,n))
print(set_1 + set_2 + n)

# 4. Пользователь вводит целое положительное число. Найти самую большую цифру в числе.
num = int(input('Введите целое положительное число: '))
n = num
max_digit = n % 10
while n:
    a = n % 10
    if a > max_digit:
        max_digit = a
        if max_digit == 9:
            break
    n = n // 10
print(f'Наибольшая цифра в {num} равна {max_digit}')

# Вар рекурс
def num_max(num):
    if num < 10:
        return num
    else:
        m = num_max(num // 10)
        return m if m > num % 10 else num % 10

print(f'The largest number is: {num_max(int(input("Enter a number: ")))}')

# 5 Задание про выручку и издержки фирмы
income = int(input('Введите выручку: '))
expense = int(input('Введите издержки: '))
net_income = income - expense
if net_income > 0:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки: {net_income / income: .2f}')
    people = int(input('Введите количество сотрудников '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {net_income / people: .2f}')
elif net_income < 0:
    print('Фирма работает с убытком')

# 6 Задание про спортсмена
while True:
    a = float(input('Старт: '))
    b = float(input('Финал: '))
    if a < 0 or b < 0:
        print('Введите положительные числа')
    else:
        days = 1
        while a < b:
            a += a * 0.1
            days += 1
        print(f'Спортсмен добьётся результатов за {days} дней.')
        break
        