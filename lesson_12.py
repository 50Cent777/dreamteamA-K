# #
# # def square(integer):
# #     s = integer ** 2
# #      return s
# f = [1, 3, 4]
#
# def square(integer):
#     return integer ** 2
#
#
#
#
# def summ(integer, string):
#     return int(integer) * str(string)
#
#
# # g = summ(string='astr', integer=10)
# # print(g)
# summ(string='astr', integer=10)
# print(summ(string='astr', integer=10))
#
#
# def hello():
#     return 'Hello world'
#
#
# def append():
#     s = hello()
#     return s + '!!!'
#
# # d = square(4)
# # print(d)
# # print(square(4))
#
# name = input('Your name: ')
# last_name = input('Your last_name: ')
# age = int(input('Your age: '))
#
#
# def func(name, last_name, age):
#     return f'Привет {name} {last_name}, тебе {age}!'
#
#
# q = func(name=name, last_name=last_name, age=age)
# print(q)
# name = input('Your name: ')
# last_name = input('Your last_name: ')
# age = int(input('Your age: '))
#
#
# # def func(name, last_name, age):
# #     if age < 25:
# #         return f'Привет {name} {last_name}, тебе {age} молокосос!'
# #     elif age > 25 and age < 33:
# #         return f'Привет {name} {last_name}, тебе {age} машина!'
# #     else:
# #         return f'Привет {name} {last_name}, тебе {age} дед!'
# #
# #
# # q = func(name=name, last_name=last_name, age=age)
# # print(q)
#
# name = input('Your name: ')
# last_name = input('Your last_name: ')
# age = int(input('Your age: '))
#
#
# def func(name, last_name, age):
#     if age < 25:
#         return f'Привет {name} {last_name}, тебе {age} молокосос!'
#     elif age > 25 and age < 33:
#         return f'Привет {name} {last_name}, тебе {age} машина!'
#     else:
#         return f'Привет {name} {last_name}, тебе {age} дед!'
#
# if age >= 18:
#     print(func(name=name, last_name=last_name, age=age))
# else:
#     print('Forbidden!')
#
# # q = func(name=name, last_name=last_name, age=age)
# # print(q)

# 1.Создайте функцию, которая принимает в себя две строки: first_name и last_name и возвращает строку "Привет, {имя
# фамилия".
# name = input('введи ка ur name: ')
# last_name = input('введи ка ur last_name: ')
#
#
# def func(name, last_name):
#     return f'Привет {name} {last_name}'
#
#
# print(func(name=name, last_name=last_name))


# 2. Напишите функцию, которая принимает в себя строку и в случае, если вся строка состоит из уникальных символов,
# верните True, иначе False.
# stre = input("Введите символы:")
#
#
# def funs(str):
#     if len(str) == len(set(str)):
#         return True
#     if len(str) != len(set(str)):
#         return False
#
#
# s = funs(str=stre)
# print(s)

# #3. Создайте функцию, которая примет в себя такие аргументы: Имя покемона, его уровень в виде числа и его тип.
#
# Покемон считается слабым, если его уровень меньше или равен 20, средним если его уровень выше 20 и меньше или равен
# 50. Если его уровень выше 50, то покемон считается сильным.
# Покемон может быть огненного, водяного и землянного типов.
name = input('Your name: ')
last_name = input('Your last_name: ')
age = int(input('Your age: '))


 def func(name, last_name, age):
     if age < 25:
         return f'Привет {name} {last_name}, тебе {age} молокосос!'
     elif age > 25 and age < 33:
         return f'Привет {name} {last_name}, тебе {age} машина!'
     else:
         return f'Привет {name} {last_name}, тебе {age} дед!'


q = func(name=name, last_name=last_name, age=age)
print(q)
#

