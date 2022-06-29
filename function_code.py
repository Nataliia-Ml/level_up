# import json


# def hello_world():
#     print("Hello World!")
#
# fg = hello_world()
# print("fg: -----", fg, ". Type of fg is: -----", type(fg))
#
# def empty_function():
#     pass
# empty_function()
#
# def get_data(ar):
#     if ar==0:
#         return
#     return 23
#
# df = get_data(0)
# print("df: -----", df, ". Type of df is: -----", type(df))


# def add(a, b):
#     '''
#     Фукнции с позиционними аргументами
#     '''
#     print('a: ', a)
#     print('b: ', b)
#     return a + b


# def keyword_function(a=1, b=2):
#     '''
#     Функции с именованными аргументами
#     '''
#     print('a: ', a)
#     print('b: ', b)
#     return a + b

# df = add(b=3)
# print("df: -----", df, ". Type of df is: -----", type(df))
# sf = keyword_function(b=4)
# print("sf: -----", sf, ". Type of sf is: -----", type(sf))
# def mixed_function(a, b=2, c=3):
#     '''
#     Функции с позиционними и именованными аргументами
#     '''
#     print("b: -----", b, ". Type of b is: -----", type(b))
#     return a + b + c

# mf = mixed_function(2, 3)
# print("mf: -----", mf, ". Type of mf is: -----", type(mf))
# def many(*args, **kwargs):
#     '''
#     *args, **kwargs
#     '''
#     print('args: ', args)
#     print('type(args): ', type(args))
#     print('kwargs: ', kwargs)
#     print('type(kwargs): ', type(kwargs))
#
# many(1, 2, 3, 4,5,6,7,8,9, name="Mike", job="programmer")


# from typing import Tuple, Any
# def many(name: str, job: str, salary: float, age: int = None) -> Tuple[int, str]:
#     print('name: ', name)
#     print('job: ', job)
#     print('age: ', age)
#     print('salary: ', salary)
#     return age, name
# age_data, _ = many(name="Mike", job="programmer", age=10, salary=2.5)


# def many(**kwargs):
#     '''
#         *args, **kwargs
#         '''
#     print('kwargs: ', kwargs)
#     name = kwargs['name']
#     print('name: ', name)
#
# many(name="Mike", job="programmer", age=10, salary=2.5)



# # Особенность работи инструкции return
# # Инструкциия return преривает дальнейшую работу функции
# def my_max(a, b):
#     print('a: ', a)
#     print('b: ', b)
#     if a > b:
#         print('a: ', a)
#         return a
#     elif b > a:
#         print('b: ', b)
#         return b
#     else:
#         return 'equal'


# def function_return_some_params():
#     a = 1
#     b = 2
#     return a, b

# def function_return_some_input_params(a, b):
#     return a, b


# # Область видимость и глобальные переменные

# def function_a():
#     a = 1
#     b = 2
#     return a + b
# sum = function_a()
# print("sum: -----", sum, ". Type of sum is: -----", type(sum))
# print("a: -----", a, ". Type of a is: -----", type(a))


# def function_b():
#     c = 3
#     return a + c

def consts():
    a = 1
    b = 2
    return a, b

# def function_a():
#     # global a
#     # a = 1
#     b = 2
#     return a + b
def function_a():
    a, b = consts()
    return a + b

sum = function_a()
print("sum: -----", sum, ". Type of sum is: -----", type(sum))
print("a: -----", a, ". Type of a is: -----", type(a))


# def function_b():
#     c = 3
#     return a + c

x = 5
def main():
    hello_world()
#     # Пустая функция
    print(empty_function())

    # # Фукнции с позиционними аргументами
    # print(add(100, 2000))
    # print(add(2, 1))
    # print(add('ASDSD', 'qwew'))

    # # # Недостаточно аргументов
    # print(add(1))
    # print(add('ASDSD'))

    # print(add(a=2, b=3))
    # total = add(b=4, a=5)
    # print(total)

    # # Неправильное название аргументов
    # a=2
    # b=3
    # print(add(a=a, b=b))
    # add(c=5, d=2)

    # Фукнции с именованными аргументами
    # print(keyword_function(a=5, b=4))
    # print(keyword_function(b=4, a=5))
    # print(keyword_function(4, b=5))
    # print(keyword_function(a=5))

    # Фукнции с позиционними и именованными аргументами
    # mixed_function(b=4, c=5)
    # print(mixed_function(68, c=5, b=4))
    # print(mixed_function(1))
 
    # *args, **kwargs
    # many(1, 2, 3, 4,5,6,7,8,9, name="Mike", job="programmer")
    # many(name="Mike", job="programmer", age=10, salary=2.5)
    # many({1:2, 3:4, 5:6, 7:8}, name="Mike", job="programmer", age=10, salary=2.5)

    # Особенность работи инструкции return
    # Инструкциия return преривает дальнейшую работу функции
    # a = 1
    # b = 2
    # print(my_max(a, b))
    # qwerty, _ = function_return_some_params()
    # print('_: ', _)
    # print('qwerty: ', qwerty)
    # print(function_return_some_params())
    # print(type(function_return_some_params()))

    # print(function_return_some_input_params(a, b))

    # Область видимость и глобальные переменные
    # print(function_a())
    # print(function_b())

    # Local область видимости
    # def add_two(a):
    #     global x
    #     return a + x
    # print(add_two(3))
    # x = 3
    # print(x)

    # Local область видимости
    # def add_four(a):
    #     x = 2
    #     def add_some():
    #         b = 3
    #         print("x = " + str(x))
    #         return a + x
    #     return add_some()
    # print(add_four(5))

    # Global область видимости
    # def fun():
    #     global x
    #     x = 4
    #     print(x+3)
    # print(fun())
    # print(x)

    # Анонимные функции, инструкция lambda
#     import math
#     sin_x_y = lambda x, y: math.sin(x) + y
#     print('sin_x_y: ', sin_x_y(1, 2))
#     func_add = lambda x, y: x + y
#     print(func_add(1, 2))
#     # print(func_add('a', 'b'))
#     print((lambda x, y: x + y)(1, 2))
#     print((lambda x, y: x + y)('a', 'b'))
#     func = lambda *args: list(args)
#     print(func(1, 2, 3, 4,6,8,9,4))

# if __name__ == '__main__':
#     age_data, _ = many(name="Mike", job="programmer", age=10, salary=2.5)
#     print("age_data: -----", age_data, ". Type of age_data is: -----", type(age_data))
    # main()
