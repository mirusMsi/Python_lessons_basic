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


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]


if __name__ == '__main__':
    want = "yes"
    amount_tasks = 3
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
