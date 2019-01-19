# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):

    fibonacci = []
    answers = []

    def fibonacci_count(before, number, amount, array):
        array.append(number)
        if amount > 1:
            fibonacci_count(number, before + number, amount - 1, array)

    fibonacci_count(0, 1, m, fibonacci)

    for x in range(n - 1, m):
        answers.append(fibonacci[x])

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

print(fibonacci(5, 12))

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
print(sort_to_max([8, 7, 6, 5, 4, 3, 2, 1, 0]))

array = ['мак', 'просо', 'мак', 'мак', 'непросо', 'мак', 'просо', 'просо', 'просо', 'мак']
print(own_filter(lambda x: x == 'мак' or x == "непросо", array))
