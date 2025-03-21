# def first(txt):
#     return txt.upper()
# # print(first("Hello"))
# second = first
# def third(txt):
#     return txt.lower()
# # print(second("World"))
#
# def greet(func):
#     greeting = func("Hi, I am created by a function passed as an argument")
#     print(greeting)
#
# greet(first)
# greet(second)
# greet(third)
from inspect import ClosureVars

# def create_adder(x):
#     def adder(y):
#         return x + y
#     return adder
#
# add_15 = create_adder(15)
# print(type(add_15))
# print(add_15(10))
# print(add_15(100))

# Closure
# def say_name(name):
#     def say_goodbye():
#         print("Say me good bye,", name)
#
#     return say_goodbye
#
# f1 = say_name("Alexander")
# f2 = say_name("Python")
# f1()
# f2()

# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
# c1 = counter(100)
# c2 = counter()
# for _ in range(5):
#     print(c1(), c2())

# def func_decorator(func):
#     def wrapper(title1, title2):
#         print("Do something before call to a new function")
#         func(title1, title2)
#         print("Do something after call to a new function")
#
#     return wrapper
#
# def some_func(title1, title2):
#     print(f"Call to function some_func, {title1}, and some number with any sense is {title2}")
#
# some_func = func_decorator(some_func)
# some_func("Python forever", 4)

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         c = []
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#         c.extend(args)
#         return c
#     return wrapper_do_twice
# @do_twice
# def custom_sum(a, b):
#     print(a + b)
# # custom_sum = do_twice(custom_sum)
# # lst = custom_sum(5, 7)
# # print(lst)
# @do_twice
# def custom_sum_many_args(*args):
#     print(sum(args))
#
# lst2 = custom_sum_many_args(3, 5, 8, 90, 500)
# print(lst2)

import time
from multiprocessing.sharedctypes import class_cache
from multiprocessing.spawn import old_main_modules

import prime


# @timer
# def does_something_to_waste_time(num_times):
#     for _ in range(num_times):
#         s = sum([num**2 for num in range(10_000)])
#         # print(s)
# does_something_to_waste_time(999)

# a = 18, b = 24 => 24-18=6 => 18-6=12 12 -6 = 6
# @prime.timer
# def gcd_slow(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
# print(gcd_slow(2,10000_000))
#
# @prime.timer
# def gcd_fast(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(gcd_fast(2, 10000_000))


# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Not valid coordinates range")
#
#     def get_coord(self):
#         return self.x, self.y
#
# v = Vector(1, 300)
# # print(Vector.get_coord(v))
# print(v.get_coord())
# print(Vector.validate(70))

class Person:
    def __init__(self, fullname, age, id, high):
        self.__fullname = fullname.split()
        self.__age = age
        self.__id = id
        self.__high = high

    @classmethod
    def verify_name(cls, fullname):
        if type(fullname) != str:
            raise TypeError("Fullname should be a string")
        