from timeit import timeit

x = 3
y = x

# Types of data
# The following types are not mutual
# Integer - int - 3; -34
# Float   - float - 0.12; 100.3, 10.0
# Boolean - bool  - True, False
# tuple(кортеж) - tuple - (1, 3, 6)
# None (ничто) - NoneType
# string - str - "Hello, world!"

# The following types are mutual
# list(список) - list - [1, 2, 2, 2]
# set(множество/набор) - set - {2, 3}
# dictionary(словарь) - dict - {2:4, 6:89}
# user-defined classes

# name = 'Alexander'
# num = 20
# num2 = num
# num3 = 20
# print(id(num))
# print(id(num2))
# print(id(num3))
# print(id(name))
# print(id('Alexander'))

# long_str = """This is a
#  very,
#  very,
#  long
#     string"""
# print(long_str)
# print(type(long_str))

# print(name)
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.count('a'))
# print(dir(name))

# help(name.count)
# print(len(name))
# print(name[0:4])
# print(name[:4])
# print(name[4:])
# print(name[1:6:2])
#
# print(name[::2])
#
# print(name[::-1])
# print(name[-6])
# print(name[5::-1])

# num = int(input("Enter the number: "))
# num = input("Enter the number: ")
# print(num)
# # print(type(num))
# print(int(num) + 100)
import math
# print(int(pow(4.0,3.0)))
# print(pow(4,0.5))
# x = 4
# print(pow(x, 2))
# print = "hello"  - Don't do it!!!
# popul = 9_000_000_001.5
# half = popul / 2
# print(half)
# print(round(half))
# print(math.ceil(half))
# print(math.floor(half))

# print(dir(math))

# print(pow(2,-2))
# print(math.pi)

# exist = True
# print(exist)
# print(type(exist))
# print(dir(exist))

# print(5 <= 3)

# print("Hello" == "Hello ")

# print("Hello" == 'Hello')
# print("Hella" > "HellZ")

# my_list = [3, -0.34, "Hello, world", False, None]
# print(type(my_list))
# print(my_list)
# print(dir(my_list))
# print(len(my_list))
# print(my_list[::-1])
# str1 = "Hello,    world!"
# lst1 = list(str1)
# print(lst1)
# print(len(lst1))
# empty_list = []
# print(id(my_list))
# print(len(empty_list))
# print(my_list[2])
# my_list[2] = -444
# print(my_list)
# print(id(my_list))
# del my_list[1]
# print(my_list)
# print(id(my_list))

# lst_nums = [2.5, 5, 4.0, 3.7, -0.65]
#
# print(min(lst_nums))
# print(max(lst_nums))
# print(sum(lst_nums))
# # len
# print(sum(lst_nums)/len(lst_nums))
#
# lst_nums.append(2.2)
# print(lst_nums)
# lst_nums2 = [2.5, 5, 4.0, 3.7, -0.65, 2.2]
# lst_nums5 = lst_nums
# print(lst_nums == lst_nums2)
# print(id(lst_nums))
# print(id(lst_nums2))
# print(id(lst_nums5))
# print(lst_nums is lst_nums2)
# print(lst_nums is lst_nums5)
# lst_nums5.append("This is a new element") # appends a new single element to the end of the list
# print(lst_nums[-1])
# print(lst_nums2[-1])
# lst_nums3 = lst_nums2.copy()
# print(lst_nums3)
# print(lst_nums2 is lst_nums3)
# lst10 = list(lst_nums2) # it creates a new object on the base of the original list
# lst20 = lst_nums2[:-1:1]
# print(lst20)
# print(lst20 is lst_nums2)

# st = lst_nums5[-1]
# ls = list(st)
# print(ls)
# ls2 = st.split()
# print(ls2)
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


# sl = slice(2,3,1)
# rn = range(2,5,2)
# print(fruits[sl])
# print(type(slice))
# print(sl)
# if "orange" in fruits:
#     print("Yes, the orange is in our basket")
# print("It prints any way")

# print("kiwi" in fruits)
#
# fruits[1:3] = ["blackcurrant", "watermelon"]
# fruits[4:5] = ["peach", "bean"]
# fruits[4] = ["kiwi", "plum", "apricot"]
#
# print(fruits)
# print(fruits[4][1])
#
# # how to append (extend) several elements to the end of the list
#
# tropical_fruits = ["pineapple", "papaya", "passion fruit"]
# fruits.extend(tropical_fruits)
# print(fruits)
# nested_list = [1,[2, [3, [4, [5]]]]]
# print(nested_list)
# print(len(nested_list))
# print(nested_list[1][1][1][1][0])
# fruits.append("orange")
# # lst2 = [2, 2, 2, 4, 3, 2, 4, 3, 2]
# # print(lst2)
# print(fruits)
# x = fruits.remove("orange")
# fruits[3].remove("kiwi")
# # fruits.remove("potato") # receives an error because no such element exists
# print(fruits)
# print(x)
# y = fruits.pop(1)
# print(fruits)
# print(y)
# del fruits[2]
# fruits.clear()
# print(fruits)
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# fruits[1:3] = ["blackcurrant", "watermelon"]
# fruits[4:5] = ["peach", "bean"]
# # fruits[4] = ["kiwi", "plum", "apricot"]
# tropical_fruits = ["pineapple", "papaya", "passion fruit"]
# fruits.extend(tropical_fruits)

# for i in fruits:
#     print(i)

# lst2 = [2, 2, 2, 4, 3, 2, 4, 3, 2]
# lst = []
# for index in lst2:
#     if index != 2:
#         lst.append(index)
# lst2 = lst
# print(lst2)

# new_list = [] # create a new empty list
#
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)

# print(new_list)

# list comprehension

# new_list = [x for x in fruits if "a" in x]
# print([x for x in fruits if "a" in x])
#
# # variable = [item for item in iterable if condition == True]
#
# str1 = "Hello, 115, world-345!"
# print([symbol for symbol in str1 if str.isspace(symbol)])


# lst3 = [x*x+20 for x in range(10)]
# print(lst3)

# print([num for num in range(21) if num % 2 == 0])

# new_fruits = [x.upper() for x in fruits]
# print(new_fruits)

# name = "Alexander"
# num = float(input("Enter some number: "))

# print("The entered number is ", num," You", name, " are a king!")
# print(f"The entered number is {num:.3f}. You {name} are a king")

# print(f"The price is {20 * 59} dollars. You {name} are a king")
#
#
# price = int(input("Input the price: "))
# mes = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
# print(mes)

# for i in range(5):
#     for j in range(5):
#         print("* ", end="")
#     print()

# greet = [f"Hello {x}" for x in fruits]
# print(greet)
# print(fruits)


# newlist = []
# for i in fruits:
#     if i != 'banana':
#         newlist.append(i)
#     else:
#         newlist.append('orange')

# print([x if x!= 'banana' else 'orange' for x in fruits])
# print(newlist)

# print([[x for x in range(5)] for y in range(5)])


# lst1 = [1, 4, 5, 7, 34, 67]
# lst2 = [2, 4, 6, 7, 58, 66, 69]
# lst3 = []
#
# i, j = 0, 0
#
# while i < len(lst1) and len(lst2):
#     if lst1[i] <= lst2[j]:
#         lst3.append(lst1[i])
#         i+=1
#         if i >= len(lst1):
#             while j < len(lst2):
#                 lst3.append(lst2[j])
#                 j+=1
#     else:
#         lst3.append(lst2[j])
#         j+=1
#         if j >= len(lst2):
#             while i <len(lst1):
#                 lst3.append(lst1[i])
#                 i+=1
# print(lst1)
# print(lst2)
# print(lst3)

# lst = [56, 13, 37, 0, 5, 37, 34, 0, -4]
#
# for j in range(len(lst)-1):
#     for i in range(len(lst)-1):
#         if lst[i] > lst[i+1]:
#             lst[i], lst[i+1] = lst[i+1], lst[i]
#
# print(lst)

# num = int(input("Enter number of lines: "))
# pascal = []
# for i in range(num):
#     pascal.append([1]+[0]*num)
#
# for i in range(1,num):
#     for j in range(1, i+1):
#         pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
#
# for i in range(num):
#     print(" " * (num - i -1), end="")
#     for j in range(i+1):
#         print(pascal[i][j], end=" ")
#     print()

# print(pascal)

# tuple - Кортеж

# tpl = ("apple", "banana", "cherry")
# print(id(tpl))
# tpl2 = ("cherry", "apple", "banana")
# print(tpl == tpl2)
# print(type(tpl))
# print(tpl[1])
# print(dir(tpl2))
# print(tpl.index("cherry"))

# for i in tpl:
#     print(i)

# RAM - random access memory

# tpl += tpl2
# print(tpl)
# print(id(tpl))

# first_hundred = []
# print(type(first_hundred))
# for i in range(100):
#     first_hundred.append(i)
#
# print(first_hundred)
# first_hundred = tuple(first_hundred)
# print(first_hundred)


import time

# lst = [ i for i in range(50_000_000)]
# lst = list(range(50_000_000))
# tpl = tuple(range(50_000_000))
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# gen = ( i for i in range(5))
# print(gen.__sizeof__())
# tpl = tuple(gen)
# print(tpl.__sizeof__())

# start = time.time()
# for i in range(len(tpl)):
#     for j in range(10):
#         a = tpl[i]
# print("Total lookup time for tuple: ", time.time() - start)
#
# start = time.time()
# for i in range(len(lst)):
#     for j in range(10):
#         a = lst[i]
# print("Total lookup time for list: ", time.time() - start)

# green = "apple"
# fruits = (green, "banana", "cherry", "kiwi", "plum")
# print(fruits)
#
# *green, yellow, red, blue = fruits
# print(green)

# tpl = ((1,2),(3,4),(5,6))
# print(tpl[1][1])
#
# tpl3 = ([1,2],(3,4))
# print(tpl3)
# print(tpl3[0])
# print()
#
# tpl3[0][1] = ["Hello, world", (4,9), [[("Hello", "World"), True], None, -34.56]]
# tpl3[0][1][2][0][0] = 5
# print(tpl3)

# inp = [(6,7), (4,5), (2,3), (2,8)]
# # output [(2,3), (4,5), (2,8), (6,7)]
#
# lst = len(inp)
# for i in range(lst):
#     for j in range(lst-i-1):
#         if inp[j][0] + inp[j][1] > inp[j+1][0] + inp[j+1][1]:
#             inp[j], inp[j+1] = inp[j+1], inp[j]
#
# print(inp)

# x = [5,6,7]
#
# print(not isinstance(x, (int, str, float)))

# lst = [4, 5, 7, "Hello, Buddy", [], (1,2,3), 5, 56, True]
# # print(lst[3])
#
# cnt = 0
# for num in lst:
#     if isinstance(num, tuple):
#         break
#     cnt += 1
#
# print(cnt)

# time.time()


# def my_first():
#     print("Hello")
#
# x = my_first()
# p = my_first
# print(x)

# def hello(name, city):
#     print("Hello", name)
#     print("You live in", city)
#
# hello("Alexander", "Ashdod")


# def max2(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
# # print(max2(23, 67))
#
# def max3(x, y, z):
#     tmp = max2(y, z)
#
#     return max2(x, tmp)
#
# print(max3(67, 100, 0))


# def fun_country(country="You forgot to put country"):
#     print("I am from " + country)
#
# fun_country("Norway")
# fun_country("USA")
# fun_country()

# def call_child(*kids):
#     print("The name of child is ")
#     for i in kids:
#         print(i)
#
# call_child("Mary", "Sam", "Bob", "Emily")

# def fibo_test(x):
#     a, b, num = 0, 1, 0
#
#     if 1 >= x:
#         return x
#
#     while x > 1:
#         num = a + b
#         a = b
#         b = num
#         x -= 1
#     return num
#
#
# num_fib = int(input("Enter the number: "))
#
# print(fibo_test(num_fib))


# _str = "this year 2025 is very challenging"

# lst = _str.split()
# print(lst)

# lst2 = list(_str)
# print(lst2)

# strg = 'this year 2025 is very challenging'
# lst1 = []
# for i in strg:
#     if i.isalpha():
#         lst1.append(i)
# print(lst1)

# print([x for x in strg if x.isalpha()])


# Fibonacci
# 1,1,2,3,5,8,13,21...

# def fibo(x):
#     num =890
#     seq = [1, 1]
#     for i in range(2,x):
#         # next_num = seq[i-1] + seq[i-2]
#         # seq.append(next_num)
#         seq.append(seq[i-1] + seq[i-2])
#     return seq
#
# num = int(input("Enter the number of fibonacci elements you want: "))
# # print(fibo(num))
#
#
# x = [int((0.5 + 5**0.5/2)**n / 5**0.5 +0.5) for n in range(1, num+1)]
# print(x)

# def fibo_rec(n):
#     if n in {0, 1}:
#         return n
#     # print(n)
#     return fibo_rec(n-1) + fibo_rec(n-2)
#
# print([fibo_rec(n) for n in range(1, num+1)])

# import platform
# print(platform.python_implementation())

# def my_fun(x):
#     x = 20
#     return x
#
# x = 10
# my_fun(x)
#
# print(my_fun(x))

# def my_list(lst):
#     for i in range(len(lst)):
#         lst[i]+=10
#
# lst2 = [1, 2, 4, 7]
# my_list(lst2)
# print(lst2)

# fruits = ['banana', 'orange', 'kiwi', 'peach', '4' ]
# fruits.sort()
# print(fruits)
#
# print(sorted(fruits, key=len, reverse=True))
# print(fruits)

# veget = ['potato', 'tomato', 'cucumber', 'corn']
#
# lst3 = veget + fruits
# print(lst3)
#
# veget += fruits
# print(veget)

# for x in veget:
#     fruits.append(x)
#
# print(fruits)

# prime numbers
#
# from prime import fast_prime, prime_classic
#
# def list_of_primes_classic(num:int):
#
#     """This function builds a list and return it with specified amount of prime number
#     using classic algorithm. num - the maximal number that limits the prime numbers
#     """
#
#     ls = []
#     for i in range(num+1):
#         if prime_classic(i):
#             ls.append(i)
#     return ls
#
#
# def list_of_primes_fast(num):
#     ls = []
#     for i in range(num+1):
#         if fast_prime(i):
#             ls.append(i)
#     return ls
#
# import time
#
# start = time.time()
# list_of_primes_fast(10000)
# print(time.time() - start)
#
#
# start = time.time()
# list_of_primes_classic(10000)
# print(time.time() - start)
#
# help(list_of_primes_classic)
# help(list_of_primes_fast)

# greeting = lambda : print("Hello, world!")
# greeting()
#
# # greet_user = lambda name : print("Hello," , name)
# # greet_user('Alexander')
#
# (lambda name : print("Hello," , name))('Ilon Musk')
#
# x = lambda x: x+1
# print(x(2))

# lst = [5, -14, (lambda x: x**3)(2), -44]
# print(lst)

# num = int(input("Enter the number: "))
# lst = ["number is", num, "square is", (lambda x: x*x)(num), True]
# print(lst)

# def get_filter(l, filter=None):
#     if filter is None:
#         return l
#     res = []
#     for x in l:
#         if filter(x):
#             res.append(x)
#     return res
# print(lst)
# print(get_filter(lst, lambda x: x%2 ==0))
# print(get_filter(lst, lambda x: x>0 and x%2==0))

# map filter

# lst2 = [1, 3, 6, 20, 90]
# for i in range(len(lst2)):
#     lst2[i]*=lst2[i]
# print(lst2)


# m = map(lambda x:x*x, lst2)
# print(*lst2)

# f = filter(lambda x: x%3==0, lst2)
# print(*f)

# lis = [[1,'s',2],[3,'a',3],[-2,'w',10]]
# print(sorted(lis))
# print(sorted(lis, key=lambda lis: lis[2], reverse=True))
# print(sorted(lis, key=lambda lis: lis[0]**2))


# str1 = "We are very happy to meet the neighbours and congratulate them with a new year"
# ls_str=str1.split()
# print(ls_str)
# print(sorted(ls_str, key=lambda ls_str: len(ls_str)))
# print(len(ls_str))
# print(sum(map(len, ls_str))/len(ls_str))


# lst_subseq = [10, 22, 20, 30, 45, 40, 50, 30, 30, 20]

# def longest_increasing_subsequence(arr):
#     if not arr:
#         return 0
#
#     n = len(arr)
#     dp = [1]*n
#
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#
#     return max(dp)

# print(longest_increasing_subsequence(lst_subseq))

# def long_sub(lst):
#     if not lst:
#         return 0
#     num = 1
#     arr = []
#     for i in range(len(lst) - 1):
#         if lst[i] < lst[i+1]:
#             num += 1
#         else:
#             arr.append(num)
#             num = 1
#     return max(arr)
#
# arr = [10, 20, 30, 40, 50, 30, 30, 20]
# print(long_sub(arr))

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst3 = [7, 8, 9]
#
# def add_three_given_lists(a, b, c):
#     return list(map(lambda a, b, c: a+b+c, a, b, c))
#
# print(add_three_given_lists(lst1, lst2, lst3))

# size = 9
#
# for i in range(size):
#     if i == size-1 or i == 0:
#         print(size*'*')
#     else:
#         print(' '*(size-i-1)+'*')

# st = {'a', 1, 4, 8, 3, 1,(3,(4,8, 'tre'), 4), 'g'}
# print(st)
# print(len(st))

# st2 = {3, 'a', 7, *[5, 'f', 7]}
# print(st2)


# strn = 'abracadabra'
# set1 = set(strn)
# print(set1)

# new_str = "|".join(set1)
# print(new_str)

# set1.add('t')
# print(set1)
# set1.remove('d')
# print(set1)
# # set1.remove('d') # cannot remove the element that doesn't exist - receives error
# set1.discard('d')
# set1.discard('b')
# print(set1)

# st1 = {'a', 'b', 'c'}
# st2 = {'d', 'e'}
# print(id(st1))
# st1.update(st2)
# print(st1)
# print(id(st1))

# fruits = {"apple", "banana", "cherry"}
# tropical = ["mango", "pineapple"]
# fruits.update(tropical)
# print(fruits)
#
# new_fruits = fruits.union(tropical)
# print(new_fruits)
# for i in range(3):
#     fruits.pop()
# print(fruits)

# fruits.clear()

# del fruits
# print(fruits)

# intersection

# st1 = {2, 6, 9, 4}
# st2 = {4, 8, 6, -1}
# st11 = {10, 20, 6, 4, "Hello"}

# st3 = st1.intersection(st2)
# print(st3)
# st4 = st1 & st2 & st11 # intersection
# print(st4)
# st5 = st1.union(st2)
# print(st5)
# st6 = st1 | st2 | st11 # union
# print(st6)

# print(st1)
# print(st2)
# print(st1.difference(st2))
# print(st2.difference(st1))
#
# print(st1 - st2) # difference

# st1.difference_update(st2)
# st1-=st2 # the same action as in the row above
# print(st1)

# st1.intersection_update(st2)
# st1 &= st2 # the same action as in the row above
# print(st1)

# st1 |= st2 # makes an action like union update
# print(st1)

# print(st1.symmetric_difference(st2))
# print(st1 ^ st2)
#
# # st1.symmetric_difference_update(st2)
# st1^=st2
# print(st1)

# print(dir(st1))

# st1 = {True, 2, False}
# st2 = {False, 2, 1, 0, 5, True}
#
# print(st1)
# print(st2)
# print(st1.issubset(st2))
# print(st2.issuperset(st1))

lst1 = list(range(1000))
# lst2 = list(range(100))
# lst1 += lst2
# # print(lst1)
# lst1 = set(lst1)
# print(lst1)

# print(hash(50))
# for i in lst1:
#     i*=1000
#     print(i, end=", ")
# for i in lst1:
#     print(i, end=", ")
# import time
# MAX_VALUE = 80_000_000
# SEARCH_ITEM = 79_999_900
#
# def measure_time(data):
#     start = time.time()
#     if SEARCH_ITEM in data:
#         return time.time() - start
# st = set(range(1, MAX_VALUE))
# lst = list(range(1, MAX_VALUE))
# print(f"Set search time: {measure_time(st)}")
# print(f"List search time: {measure_time(lst)}")

# st = {"Hello", "world", "we", "learn", "python"}
# print(st)
# st.add("Bye-bye")
# print(st)
# st = frozenset(st)
# print(type(st))
# print(st)
# st = set(st)

# size = 6
# # for i in range(size+1):
# #     print("*" * i)
#
# for i in range(size+1):
#     print(" "*(size-i)+"*"*i)

from pprint import pprint

# Dictionary
# thisdict = {
#     "brand":"Ford",
#     "model": "Mustang",
#     "Year of building": 1968,
#     "Year of product": 1968,
#     "color": ["red", "white", "blue"]}
#
# print(type(thisdict))
# print(len(thisdict))
# pprint.pprint(thisdict)
#
# x = thisdict.get("Model") # not case sensitive
# print(x)

dct = dict(name="John", age=36, country="Ireland", city='Dublin', car='Rover')
# pprint(dct)
dct["watch"] = "Seiko"
#
# dct["car"] = "Audi"
# pprint(dct)
# print(dct.keys())
# print(dct.values())
# print(dct.items())
# if "age" in dct:
#     print("Yes")
# else:
#     print("No")
# dct.update({"age": 40})
# pprint(dct)
#
# print(dct.pop("car"))
# pprint(dct)
#
# print(dct.popitem())
# pprint(dct)

# for x in dct:
#     print(x, dct[x])
#
# for x in dct.keys():
#     print(x)

# for x in dct.values():
#     print(x)
#
# for x in dct.items():
#     print(x, x[1])

# for x, y in dct.items():
#     print(x, y)
#
# dct2 = dct.copy()
# pprint(dct2)
# pprint(dct == dct2)
# dct3 = dict(dct)


# myfamily = {
#     "child1":{
#         "name": "John",
#         "year": 2001
#     },
#     "child2":{
#         "name": "Mary",
#         "year": 2005,
#         "hobby": "singing"
#     }
# }
# # pprint(myfamily)
# print(myfamily["child1"])
# print(myfamily["child1"]["name"])

# list: search (x in list) O(n) - linear; get by index (list[i]) O(1)
# dictionary: search (x in dict) O(1) - constant; dict[key] O(1)

# import timeit
# big_list = list(range(70_000_000))
# # lst = [i for i in range(1000)]
# big_dict = {i: None for i in range(70_000_000)}
# print(big_dict.__sizeof__())
# print(big_list.__sizeof__())
# target = 999_999

# list_time = timeit.timeit(lambda : target in big_list, number=10)
# print(f"Search in list took: {list_time:.8f} seconds")
#
# dict_time = timeit.timeit(lambda : target in big_dict, number=10)
# print(f"Search in dict took: {dict_time:.8f} seconds")

# Create dictionary
# 1 method

# x = ("key1", "key2", "key3")
# y = 0
#
# new_dict = dict.fromkeys(x, y)
# print(new_dict)

# 2 method
# keys = ('a', 'b', 'c')
# values = (1, 2, 3)
# dict2 = {keys[i]:values[i] for i in range(len(keys))}
# print(dict2)
#
# # 3 method
# dict3 = dict(zip(keys, values))
# print(dict3)

# st = "12 31 4 53 6 7 4 90 8 7 56 3 42"
# my_dict = {int(k): int(k)*2 for k in st.split() if int(k)%2 == 0}
# print(my_dict)

# wow {'w': 2, 'o':1}

# st = "Hello, Israel. We learn DevOps in Specter college. Python is wonderful language"
#
# def create_sym_dict(input_string):
#     symbol_dict = {}
#
#     for symbol in input_string:
#         if symbol in symbol_dict:
#             symbol_dict[symbol] += 1
#         else:
#             symbol_dict[symbol] = 1
#     return symbol_dict
#
# res = create_sym_dict(st.lower().replace(" ",""))
# print(res)

# empty_dict = dict.fromkeys(["apple", "ball", "orange"])
# print(empty_dict)
# nonempty_dict = dict.fromkeys(["apple", "ball", "orange"], "xyz")
# print(nonempty_dict)

# x = {1:2, 3:4, 4:3, 2:1, 0:0}
# print(x)
# print(sorted(x))
# print(dict(sorted(x.items())))
# print(dict(sorted(x.items(), key=lambda item: item[1])))
# print({k:v for k, v in sorted(x.items(), key=lambda item: item[1])})

# def func(a=0, b=0):
#     return a + b
#
# my_dict = {'a':2, 'b':3}
# # result = func(my_dict['a'], my_dict['b'])
# result = func(**my_dict)
# print(result)
# print(*my_dict)

# num = [2, 18, 5, 7, 2, 32, 6, 5, 9, 4, 8, 7, 9, 12, 14, 14]
# my_dict = {n:num.count(n) for n in num}
# print(my_dict)

# dict1 = {'item': 'jacket', 'size': 'L', 'color': 'black'}
# dict2 = {'model': '35mr', 'quantity': 30, 'color': 'blue'}
# new = {}

# for _ in dict1:
#     new.update(dict1.items())
# for _ in dict2:
#     new.update(dict2.items())
#
# print(new)

# print({**dict1, **dict2})

# my_dict = {'age': 25, 'name': 'Roman'}
# print(my_dict.get('age'))
# my_dict.setdefault('hair color')
# print(my_dict)

# month = {1:'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май'}
# num = int(input("Введите номер месяца: "))
# print(month.get(num))

# Interactive vocabulary

# words = {}
# print("This is the dictionary that you create yourself, just enter a word: ")
# while True:
#     w = input()
#     if w == "":
#         exit()
#         # exit(1)
#     if w in words:
#         print("the word", w, "is translated as", words[w])
#     else:
#         print("Type the translation in Russian of", w)
#         words[w] = input()


# lst = ["apple", "pineapple", "green apple"]
# print({name:len(name) for name in lst})


# def cnt_words(text):
#     words_count = {}
#     for word in text.split():
#         if word in words_count:
#             words_count[word] += 1
#         else:
#             words_count[word] = 1
#     return words_count
#
# with open("C:/tmp/russian.txt", encoding='utf8') as file:
#     content = file.read()
#     # print(type(content))
# words_dict = cnt_words(content)
# # pprint(words_dict)
# pprint(sorted(words_dict.items(), key= lambda x: x[1], reverse=True))

# def my_fish(**fishes):
#     # print(f"I have {guppies} guppy fish")
#     # print(f"I have {zebras} zebra fish")
#     # print(f"I have {bettas} betta fish")
#     for name, amount in fishes.items():
#         print(f"I have {amount} {name}")
# fish = {
#     "guppies": 2,
#     "zebras":5,
#     # "bettas": 10,
#     # "salmon": 12,
#
#     "shark":1,
#     "tuna": 15
# }
# my_fish(**fish)

# lst = [1, 2, 3, 4]
# # dct = {1: {2: {3: {4:{}}}}}
#
# dct = current = {}
# for i in lst:
#     current[i] = {}
#     current = current[i]
# print(dct)

# def del_from_tuple(tpl, elem):
#     lst = list(tpl)
#     if elem in tpl:
#         lst.remove(elem)
#     return tuple(lst)
# print(del_from_tuple((1, 2, 3), -1))

# Home exercise
# Validity of parentheses "{f[t(r<dfgsdf,dsfds>)dsdfs]sdfd}"

# LIFO --- FIFO
# if 5 < 8:
#     print("Ok")
#
# print("ok") if 5 < 8 else print()


# def is_balanced(st):
#     stack = []
#     mapping = {')': '(', ']': '[', '}': '{', '>': '<'}
#
#     for char in st:
#         if char in mapping:
#             top = stack.pop() if stack else '#'
#             if mapping[char] != top:
#                 return False
#
#         elif char not in mapping.values():
#             continue
#         else:
#             stack.append(char)
#     return not stack
#
# print(is_balanced("{f[t(r<dfgsdf,dsfds>)dsdfs]sdfd}"))
# int("hello")
# dict5 = {'a': 2, 'b': 32, 'c': 10}
#
# print({v: k for k, v in dict5.items() if not isinstance(v, (list, dict, set))})

# Exceptions handling

# def division(a, b):
#     try:
#         # x, y = 5, 'a'
#         # x = x = yy
#         return a/b
#     # except  ZeroDivisionError:
#     #     return None
#     # except TypeError:
#     #     return "typeerror"
#     #
#     # except NameError as n:
#     #     return "nameerror"
#     except (ZeroDivisionError, TypeError, NameError) as exp:
#         print(exp)
#     finally:
#         print("The program continue any way")
#
# x, y = 5, 0
#
# res = division(x,y)
# print(res)


# f = open("c:/tmp/2600-h.htm", encoding='utf8')
# f.readline()
# f.close()

# try:
#     with open("c:/tmp/2600-h.htm", encoding='utf8') as f:
#         f.readline()
#         print("The file was open successfully")
# except FileNotFoundError:
#     print("No such file, try another one")
# print("Continue my work")

# try:
#     raise ValueError("This is a custom error message")
# except ValueError as e:
#     print("An error occured: ", e)
#
# try:
#     w = int(input("Enter your weight: "))
#     assert w>=0, "Only positive numbers are allowed"
# except AssertionError as e:
#     print(e)

# while True:
#     try:
#         x = int(input("Enter a number: "))
#         print("Good guy!")
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")
# def test_list_operations(num):
#     try:
#         r1 = num.length
#         print("Length of the list is:",r1)
#     except AttributeError:
#         print("Error: the list does not have a 'length' attribute")
# nums = [1, 3, 4, 0, 5, 7]
# test_list_operations(nums)

# with open("c:/tmp/file1.txt", encoding='utf8') as f:
# print(f.read())
# text = f.read()
# f.seek(20)
# txt = f.readline()
# p = f.tell()
# for line in f:
#     print(line, end="")
# print(txt)
# print(text)
# print(p)
# for each in txt:
#     print(each)     # symbols one by one are printed row by row

# with open("c:/tmp/file1.txt", 'a+') as file:
#     file.write("Hello1\n")
#     file.write("Hello2\n")
#     file.write("Hello3\n")
#     file.seek(0)
#     print(file.read())

# with open("c:/tmp/file1.txt") as file:
#     print(file.read())

# with open("c:/tmp/file1.txt") as file1:
#     print("Output of readline for specific lines is:")
#     print(*file1.readlines()[4:10], sep="")

lst = [a for a in range(10000)]
# print(lst)
dct = {k: k * k for k in range(10000)}
# print(dct)

tpl = tuple(a for a in range(10000))


# for a in tpl:
#     print(a)
# print(tpl) for i in range(:

# st = {i**2 for i in range(10) if i != 5 and i**2 % 10 in (0,4,9)}
# print(tpl.__sizeof__())
# print(lst.__sizeof__())
# print(dct.__sizeof__())
# print(st)

def func(n):
    res = []
    cnt = 0
    while cnt < n:
        res.append(cnt)
        cnt += 1


# start = time.time()
# func(1000)
# print(time.time() - start)
#
# start = time.time()
# func(100_000_000)
# print(time.time() - start)

# def func2():
#     yield 1
# # print(func2())
# print(next(func2()))
# print(next(func2()))


# def func2():
#     print("Start")
#
#     yield 1
#     print("Give me more")
#     yield 2
#     print("Finish")
#     return 1
# c = func2()
# print(next(c))
# print("It is the general flow")
# print(next(c))
# print(c)

# def func3(n):
#     cnt = 4
#     yield cnt
#     cnt = 0
#     while cnt < n:
#         yield cnt
#         cnt += 1
#
# d = func3(30)
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(4 in d)
# print(2 in d)
# print(4 in d)
# print(18 in d)
# d = func3(30)

# print(1 in d)
#
# # print(18 in d)
# print(19 in d)
#
# print(28 in d)

# s = "0123456789"
# lst = []
# lst = list(map(int, s))
# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(lst)
# print(dir(lst))
# for i in s:
#     lst.append(int(i))
# print(lst)

# iterator - Поток данных, который по востребованию выдает следующий элемент, но не хранит весь набор данных внутри себя
# generator - Функция, которая создает итератор, но не возвращает результат для всех значений, а только следующее значение
# Вместо return используется yield
# __next__() - returns next element
# __iter__() - method, that says that the element has iterable
# iterable: list, dictionary, set, tuple, string
# for iterable works - for, in, len
# for iterator works - for, in, but doesn't work len

# st = "Hello,world!"
# print(dir(st))
# iter_st = iter(st)
# lst = [1,2,3]
# iter_lst = iter(lst)
# print(len(iter_lst))
# print(next(iter_lst))
# print(next(iter_lst))
# print(next(iter_lst))
# print(next(iter_lst))

# lst = [x for x in range(1, 5000001)]
# it_lst = iter(lst)

# start = time.time()
# for i in range(1,len(lst)):
#     lst[i]=lst[i]**2
# print(lst[4990000])
# print(f"time of lst working: {time.time() - start}")
# print("Memory usage of list:",lst.__sizeof__())
#
#
# lst2 = [x for x in range(1, 5000001)]
# start = time.time()
# it_lst = map(lambda x: x**2, lst2)
# for i in range(4990000):
#     next(it_lst)
# print(next(it_lst))
# print(f"time of map iterator working: {time.time() - start}")
# print("Memory usage of map iterator:",it_lst.__sizeof__())

# car_dict = {'a': 'Mercedes-Benz', 'b': 'BMW00', 'c': 'Ferrari', 'd': 'Lamborghini', 'e': 'Jeep'}
# # _2025
#
# car_dict2 = dict(map(lambda a: (a[0],a[1]+'_2025'), car_dict.items()))
#
# print(car_dict2)
import prime

# lst = [x for x in range(1,101)]
# # print(lst)
#
# print(*filter(prime.fast_prime, lst))
# print(*filter(lambda p: not prime.fast_prime(p),lst))

# tpl = tuple(i for i in range(1000000))
# start = time.time()
# print( max(*filter(prime.fast_prime,tuple(i for i in range(10000000)))) )
# print( time.time() - start)
# start = time.time()
# print( tuple(filter(prime.fast_prime, tuple(i for i in range(10000000))))[-1] )
# print( time.time() - start)

# lst = [4, -7, 3, 5, 9, -16, 25]
# print(list(map(lambda x: x**0.5, filter(lambda y: y>=0, lst))))


# def fibo_gen():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# number = 800
# fib = fibo_gen()
# print(fib)
# for _ in range(number):
#     next(fib)
#
# print(next(fib))
# from collections.abc import Iterable
#
# def flatten(it):
#     for i in it:
#         if isinstance(i,  Iterable):
#             yield from flatten(i)
#         else:
#             yield i
#
#
# items = [[0, 1, 2], 3, 4, True, [[5], (6.56, 7)], [[[8]], 9]]
# print(list(flatten(items)))


# 7*3+1=22 /2 = 11*3+1 -17 52 26 13 40

# def collatz(n):
#     yield n
#     while n != 1:
#         n = n / 2 if n % 2 == 0 else 3 * n + 1
#         yield int(n)
# cnt = 1
# length = 1
# num = 19
# for i in range(1, num+1):
#     ls = list(collatz(i))
#     if len(ls) > length:
#         length = len(ls)
#     cnt = i
# print(list(collatz(cnt)))
# print(f"Number {num} contains {length} elements in Collatz iterable")

# zip
# a = ["John","Charles", "Mike", "Ben"]
# b = ("Jenny", "Mary", "Sarah", "Margareth")
# c = (2, 4, 3, 1)
# try:
#     x = zip(a, b, c, strict=True)
#     print(list(x))
# except ValueError as er:
#     print(er)
#
# print(list(zip(a)))
#
# for m, w in zip(a, b):
#     print(f"Man: {m}")
#     print(f"Woman: {w}")
#     Unpacking zipped list

# families = [('John', 'Jenny', 2), ('Charles', 'Mary', 4), ('Mike', 'Sarah', 3), ('Ben', 'Margareth', 1)]
#
# men, women, children = zip(*families)
# print(men)
# print(women)
# print(children)

from collections import namedtuple


# marks = (98, 80, 95)
# print(marks[2])

# Marks = namedtuple('Marks', 'Physic Chemistry Math English')
# marks = Marks((90, 92,98), 85, 100, 97)
# print(marks)
# dct = {
#     'Physic': (90, 92,98),
#     'Chemistry': 85,
#     'Math': 100,
#     'English': 97
# }
# print(dct)
# print(marks.__sizeof__())
# print(dct.__sizeof__())
# Marks_d = namedtuple('Marks_d', dct)
# print(Marks_d)

# marks2 = Marks_d(0, 0, 0, 0)
# print(marks2)

# print(marks[1])
# print(marks.Math)
# # marks[2] = 90 # not valid operation
# print(id(marks))
# marks = marks._replace(Physic=70)
# print(marks)
# print(id(marks))

# str1 = "hello"
# str2 = " world"
# x = 5
# y = 10
# print(str1.__add__(str2))
# print(x.__add__(y))

# class Cat:
#     name = 'sphinx'
#     age = 5
#     color = 'brown'
#     count = 0
#
#     def voice(self):
#         print("Meow")
#
# c1 = Cat()
# # print(dir(Cat))
# def run(self):
#     print("fast")
# Cat.run = run
# c1.run()
# print(c1.__dir__())

# Exercises
# dct1 = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # Output [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
#
# def list_of_dicts(marks):
#     keys = marks.keys()
#     vals = zip(*[marks[k] for k in keys])
#     # print(*vals)
#     res = [dict(zip(keys, v)) for v in vals]
#     return res
# print(list_of_dicts(dct1))

# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': (0, 0, 0)}
#
# dict1 = {key: value for key, value in dict1.items() if value}
# print(dict1)

lst2 = [1, 2, 3, 1, 2, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7]
# lst3 = set(lst2)
#
# dc = {}
# for i in lst3:
#     using function count()


# def first_non_repeated(ls):
#     ctr = {}
#     for i in ls:
#         if i in ctr:
#             ctr[i] += 1
#         else:
#             ctr[i] = 1
#     for i in ls:
#         if ctr[i] == 1:
#             return i
#     return
#
# print(first_non_repeated(lst2))

# dct = {'a': 1, 'b': {'c': {'d': {}}}}
# dct = {1:{}}
#
# def depth(d):
#     if isinstance(d, dict):
#         return 1 + (max(map(depth, d.values())) if d else 0)
#     return 0
#
# print(depth(dct))

# class Dog:
#     def __init__(self,name, age, tail, food):
#         self.name = name
#         self.__age = age
#         self.tail = tail
#         self.food = food
#     def __eat(self):
#         self.food += " and water"
#         print("I eat",self.food)
#
#     def meet(self):
#         print(f"my name is {self.name},I am {self.__age} years old and I have the tail {self.tail}cm")
#         self.__eat()
#
# d1 = Dog("Sharik", 5, 30, "meat")
# print(d1.name)
# d2 = Dog("Barsik", 3, 25, "Pedigree")
# # d1.eat()
# print(d1.name)
# d1.eat()
# d2.eat()
# d1.meet()
# d2.meet()

class Figure:
    name = "Figure"
    width = 2
    def draw(self):
        print("Figure drawing")

    def perim(self):
        print("Each figure should have some perimeter")

# print(Figure.width)

class Rectangle(Figure):
    """This class is description of rectangles and several actions with them,
    such as perimeter calculation and other. We created it for
    practice in Python OOP and to demonstrate how we can change help for object"""

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def perim(self):
        return 2 * (self.w + self.h)

    def __str__(self):
        return f"It is my class {self.__class__}"

r1 = Rectangle(3, 5)
# r1.draw()
# print(r1.perim())
# print(Figure.__bases__)
# print(Rectangle.__bases__)
# print(Rectangle.mro())

# help(Rectangle)
# print(r1)

# class Line:
#     color = "black"
#
# class Square(Figure, Line):
#     def __init__(self, a):
#         self.a = a
#
#     def perim(self):
#         return 4 * self.a
#
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perim(self):
#         return self.a + self.b + self.c
#
# s1 = Square(10)
# t1 = Triangle(3, 4 ,5)
# # print(s1.perim())
# # print(t1.perim())
#
# fig = [Rectangle(3, 5), Square(10), Triangle(3, 4 ,5), Triangle(6, 9 ,2), Square(7)]
# print(s1.color)
# for f in fig:
#     print(f.perim())

# class Vector(list):
#     def __str__(self):
#         return "/ ".join(map(str, self))
#
# v = Vector([1, 3, 5])
# print(type(v))
# print(v[2], v[0])
# v.append(7)
# print(v)

# from abc import ABC, abstractmethod
# class AbstractAnimal(ABC):
#     @abstractmethod
#     def speak(self):
#         print("rrrrr")


# class Dog(AbstractAnimal):
#     def speak(self):
#         print("wouf-wouf")
#     def eat(self):
#         print("nyam-nyam")
#
# d1 = Dog()
# d1.speak()
# d1.eat()
# print(dir(Dog))

# class Calculator:
#     def add(self, a, b = 0, c = 0):
#         return a + b + c
#
# calc = Calculator()
# print(calc.add(2, 4, 6))
# print(calc.add(2, 4))
# print(calc.add(2))

# class Parent:
#     def show(self):
#         print("This is the parent class")
#
# class Child(Parent):
#     def show(self):
#         print("This is child class")
#         super().show()
#
# child = Child()
# child.show()

# dunder methods - Magic methods

# class Dog:
#     pass
# print(dir(Dog))
# d1 = Dog()
# print(dir(Dog))

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         return self.__counter
#     def __str__(self):
#         return "it is my class"
# c = Counter()
# c()
# c()
# c()
# c()
#
# print(c())

class My_arr(list):
    "This is help for my ny type, just crazy list"
    def __init__(self, it):
        try:
            for i in it:
                if not isinstance(i, (int, float, bool)):
                    raise NotImplementedError
                else:
                    super().__init__(sorted(it))
            self.it = it
        except (NotImplementedError, TypeError):
            print("You can't use my type for these values")

    def __str__(self):
        return f"<<{', '.join(str(item) for item in self)}>>"

    def append(self, __object):
        try:
            if not isinstance(__object, (int, float, bool)):
                raise NotImplementedError
            else:
                super().append(__object)
                self.sort()
        except (NotImplementedError, TypeError):
            print("You can't use my type for these values")

    def __len__(self):
        cnt = 0
        for i in self:
            if i >= 0:
                cnt += 1
        return cnt

    def __call__(self, *args, **kwargs):
        print(self)
        return self

l = My_arr([4, -6, 2, 0])
print(l)
l.append(-100)
l.append(2)
l.append(-55)
print(l)
print(len(l))
new_lst = l()
print(new_lst)