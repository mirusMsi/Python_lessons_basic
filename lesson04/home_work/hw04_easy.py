import random

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


def task_1(amount):

    first = [random.randrange(-100, 100) for i in range(amount)]
    second = [x ** 2 for x in first]
    return first, second


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def task_2():

    first = ["apple", "pear", "peach", "tangerine", "plum"]
    second = ["pomegranate", "apple", "peach", "plum"]

    if len(first) > len(second):
        answer = [x for x in second if x in first]
    else:
        answer = [x for x in first if x in second]

    return answer


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

def task_3(amount):

    first = [random.randrange(-10, 1000) for i in range(amount)]
    second = [x for x in first if x % 3 == 0 and x % 4 != 0 and x > 0]

    return first, second


a, b = task_1(5)
print(a, b, sep="\n")

print(task_2())

a, b = task_3(10)
print(a, b, sep="\n")
