# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    parts = str(number).split(".")
    characters = [int(x) for x in reversed(parts[1])]

    answers = []
    transfer = 0
    steps = len(characters) - ndigits
    step = 0

    for character in characters:

        character += transfer

        if character == 10:
            answers.append("0")
            transfer = 1
        else:
            answers.append(str(character))
            transfer = 0

        if step < steps and character > 4:
            transfer = 1
            step += 1

    before = int(parts[0]) + transfer
    after = "".join(reversed(answers))

    if ndigits == 0:
        return before
    else:
        return float(str(before) + "." + after[:ndigits])


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Так как принтить нельзя, значит и ошибку не вывести, поэтому недостающие разряды буду считать за 0
# Вариант где разрядов больше 6 - сразу не счастливый

def lucky_ticket(ticket_number):

    length = len(str(ticket_number))
    if length > 6:
        return "unhappy"
    if length < 6:
        ticket_number = ticket_number * 10 ** (6 - length)

    work = [int(x) for x in str(ticket_number)]

    firs = [work[x] for x in range(0, 3)]
    second = [work[x] for x in range(3, 6)]

    if sum(firs) == sum(second):
        return "happy"
    else:
        return "unhappy"


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
