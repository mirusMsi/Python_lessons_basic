import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):

    fibonacci_array = []
    answers = []

    def fibonacci_count(before, number, amount, array):
        array.append(number)
        if amount > 1:
            fibonacci_count(number, before + number, amount - 1, array)

    fibonacci_count(0, 1, m, fibonacci_array)

    for x in range(n - 1, m):
        answers.append(fibonacci_array[x])

    return answers

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    length = len(origin_list)

    def sort(array, steps):

        for x in range(steps - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]

        steps -= 1

        if steps > 1:
            sort(array, steps)

    sort(origin_list, length)
    return origin_list


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def own_filter(functions, array):
    answer = []

    for element in array:
        if functions(element):
            answer.append(element)

    return answer


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

"""
Алгоритм следующий:
1) Если есть отрицательные координаты, то все точки смещаются (сама по себе фигура никак не меняется)
2) Точки разбиваются на те что находятся внизу dots[0, 1] и вверху dots[2, 3] (float - y.x по возростанию)
3) Определяется какие из них находятся слева, а какие справа (float - x.y по возростанию)
4) Формируется линейное представление фигуры так если бы мы именовали точки начиная с нижней левой и по часовой.
   При этом список содержит всегда следующий порядок [B - (вер.лев), C - (вер.прав),
                                                      A - (ниж.лев), D - (ниж.прав)]
5) Проверяем попарное равенство длин

"""

def check_dot(x1, y1, x2, y2, x3, y3, x4, y4):

    first = [x1, x2, x3, x4]
    first.sort()
    if first[0] < 0:
        x1 -= first[0]
        x2 -= first[0]
        x3 -= first[0]
        x4 -= first[0]

    second = [y1, y2, y3, y4]
    second.sort()
    if second[0] < 0:
        y1 -= second[0]
        y2 -= second[0]
        y3 -= second[0]
        y4 -= second[0]

    dots = [float(".".join([str(y1), str(x1)])),
            float(".".join([str(y2), str(x2)])),
            float(".".join([str(y3), str(x3)])),
            float(".".join([str(y4), str(x4)]))]

    dots.sort()

    bot = [str(dots[0]).split("."), str(dots[1]).split(".")]
    top = [str(dots[2]).split("."), str(dots[3]).split(".")]

    bot[0], bot[1] = float(".".join([bot[0][1], bot[0][0]])), float(".".join([bot[1][1], bot[1][0]]))
    top[0], top[1] = float(".".join([top[0][1], top[0][0]])), float(".".join([top[1][1], top[1][0]]))

    bot.sort()
    top.sort()

    dots.clear()
    dots.extend(bot)
    dots.extend(top)

    answer = []
    for i in dots:
        answer.append(str(i).split('.'))

    ab = math.sqrt(abs(int(answer[0][0]) - int(answer[2][0])) ** 2 + abs(int(answer[0][1]) - int(answer[2][1])) ** 2)
    cd = math.sqrt(abs(int(answer[1][0]) - int(answer[3][0])) ** 2 + abs(int(answer[1][1]) - int(answer[3][1])) ** 2)

    bc = math.sqrt(abs(int(answer[2][0]) - int(answer[3][0])) ** 2 + abs(int(answer[2][1]) - int(answer[3][1])) ** 2)
    ad = math.sqrt(abs(int(answer[0][0]) - int(answer[2][0])) ** 2 + abs(int(answer[0][1]) - int(answer[2][1])) ** 2)

    if ab == cd and bc == ad:
        return "is true"
    else:
        return "is wrong"


print(fibonacci(5, 12))

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(sort_to_max([8, 7, 6, 5, 4, 3, 2, 1, 0]))

array = ['мак', 'просо', 'мак', 'мак', 'непросо', 'мак', 'просо', 'просо', 'просо', 'мак']
print(own_filter(lambda x: x == 'мак' or x == "непросо", array))

print(check_dot(0, 1, 1, 6, 6, 5, 5, 0))
print(check_dot(0, 1, 1, 6, 6, 7, 5, 2))
print(check_dot(0, 1, -1, 6, 4, 7, 5, 2))
print(check_dot(0, 1, -1, 6, 6, 7, 5, 2))
