from os import remove

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

# 18.02.2025


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
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


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

#print("The entered number is ", num," You", name, " are a king!")
#print(f"The entered number is {num:.3f}. You {name} are a king")

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


# input two ordered by size lists into a new list that will be also ordered bi size
# currently the progam includes bug, analyze the code and find this bug (it is very small fix, that is typical bug. I already found it, just want you to find is as well. Good luck)

lst1 = [1, 4, 5, 7, 34, 67]
lst2 = [2, 4, 6, 7, 58, 66, 69]
lst3 = []

i, j = 0, 0

while i < len(lst1) and len(lst2):
    if lst1[i] <= lst2[j]:
        lst3.append(lst1[i])
        i+=1
        if i > len(lst1):
            while j < len(lst2):
                lst3.append(lst2[j])
            j+=1
    else:
        lst3.append(lst2[j])
        j+=1
        if j > len(lst2):
            while i <len(lst1):
                lst3.append(lst1[i])
                i+=1
print(lst1)
print(lst2)
print(lst3)

# 20.02.2025


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

def call_child(*kids):
    print("The name of child is ")
    for i in kids:
        print(i)

call_child("Mary", "Sam", "Bob", "Emily")
