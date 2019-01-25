import os
import re
import shutil
import sys

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create():

    for i in range(1, 10):
        path = os.path.join(os.getcwd(), ("dir_" + str(i)))
        try:
            os.mkdir(path)
        except FileExistsError:
            pass


def delete():

    for i in range(1, 10):
        os.rmdir("dir_" + str(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Как найти все кроме оканчивающихся на .py не понял
# Использую remove так как имя файла в папке уникально

def listdir():

    string = ""

    answer = os.listdir(os.getcwd())

    for i in answer:
        string = string + i + " "

    check = re.findall(r"[^\s]*\.py", string)

    for i in check:
        answer.remove(i)

    return answer

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy():
    path = re.findall(r"[^\/]*\.py", sys.argv[0])[0]
    shutil.copy(path, path[:-3] + "_copy.py")


if __name__ == '__main__':
    copy()
