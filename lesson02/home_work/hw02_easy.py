# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
<<<<<<< Updated upstream
=======


def task_3():

    stop = enter_var_int("Enter upper limit for generations (it should be integer or 'no' for exit): ")
    amount = enter_var_int("Enter amount of number which will contain list (it should be integer or 'no' for exit): ")

    first = [random.randint(1, stop) for i in range(amount)]

    second = []

    for x in first:
        if x % 2 == 0:
            second.append(x / 4)
        else:
            second.append(x * 2)

    print(first, second, sep="\n")


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
>>>>>>> Stashed changes
