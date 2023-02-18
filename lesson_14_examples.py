#1 При помощи рекурсии проверьте, является ли строка
# # палиндромом. (Палиндром это слово или фраза, которые ослева направо и справа налево: прим. "казак")


# x = str(input('Put your word mother fucker: '))
# def rec(x):
#     if x == x [::-1]:
#         print('True thats fucking Polindrome')
#     else:
#         print('False thats not fucking Polindrome')
#
# rec(x.upper())


# 3
#  Напишите функцию lambda, которая вычисляет нам площадь прямоугольника по длинам двух его сторон(длина, ширина).
#
# l = int(input("введите длину "))
# s = int(input("введите ширину "))
# a = ((lambda x, y: x * y) (l, s))
# print(a)

#2 Напишите функцию с рекурсией, которая будет вычислять нам факториал полученного числа.

# digit = int(input('Add digit: '))
# factorial = 1
# for i in range(1, digit + 1):
#     factorial = factorial * i
#
# print(f"Factorial: {factorial}")


# 4. Напишите функцию lambda, которая принимает как аргументы два числа и возвращает большее значение

# fuck = (lambda a, b: a if a>b else b)
# print(fuck(18686, 1722))

#6.. Создайте функцию-декоратор, который будет измерять время выполнения другой функции. Примените декоратор к нескольким функциям.

import time

def decor(func):
    def wrapper(*args):
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

@decor
def ff():
    print('!!!!!')
ff()