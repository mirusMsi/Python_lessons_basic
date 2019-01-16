import random
import math


def check_int(value):
    if value.lower() == 'no':
        raise SystemExit

    try:
        return int(value)
    except ValueError:
        print('Wrong enter. Pleas will try again')
        return "error"


def enter_var_int(text):
    while True:
        variable = check_int(input(text))

        if variable == "error":
            pass
        else:
            return variable


# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


def task_1():

    stop = enter_var_int("Enter upper limit for generations (it should be integer or 'no' for exit): ")
    amount = enter_var_int("Enter amount of number which will contain list (it should be integer or 'no' for exit): ")

    first = [random.randint(-stop, stop) for i in range(amount)]

    second = []

    for x in first:
        if x < 1:
            pass
        else:
            number = math.sqrt(x)
            if number % 1 > 0:
                pass
            else:
                second.append(int(number))

    print(first, second, sep="\n")


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


def task_2():

    day = {
        '01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое',
        '06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
        '11': 'одинадцатое', '12': 'двинадцатое', '13': 'тринадцатое', '14': 'четырнадцатое',
        '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое',
        '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
        '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
        '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое',
        '31': 'тридцать первое'
    }

    month = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'
    }

    while True:

        date = input("Enter date (dd.mm.yyyy): ")

        if len(date) != 10 or date.count(".") != 2:
            continue
        else:

            day_v = date[:2]
            try:
                day_name = day[day_v]
            except KeyError:
                print('You entered wrong variant of day.')
                continue

            month_v = date[3:5]
            try:
                month_name = month[month_v]
            except KeyError:
                print('You entered wrong variant of month.')
                continue

            year_v = date[6:]
            try:
                int(year_v)
                year_name = year_v
            except ValueError:
                print('You entered wrong variant of year.')
                continue

        print(f"{day_name} {month_name} {year_name} года")
        break


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


def task_3():

    amount = enter_var_int("Enter amount of number which will contain list (it should be integer or 'no' for exit): ")
    count = [random.randint(-100, 100) for i in range(amount)]

    print(count)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


def task_4():

    first = [random.randint(0, 18) for i in range(20)]
    second = []

    print(first)

    for x in first:
        if second.count(x) == 0:
            second.append(x)

    second.sort()
    print(second)
    second.clear()

    for x in first:
        if first.count(x) == 1:
            second.append(x)
    second.sort()
    print(second)


if __name__ == '__main__':
    want = "yes"
    amount_tasks = 4
    welcome = f"Enter task's number which you want to check (integer from 1 to {amount_tasks} or 'no' for exit): "

    while True:
        task = input(welcome)

        if task.lower() == 'no':
            want = task.lower()
            break
        else:
            try:
                int(task)
                task = int(task)
                if 0 < task <= amount_tasks:
                    break
                else:
                    print('You entered incorrect number, please will try again.')
            except ValueError:
                print('You entered not integer, please will try again.')

    if want == 'yes':
        num = ("task_" + str(task))
        fun = globals()[num]
        fun()
