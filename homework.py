# class Person:
#     def __init__(self, name,surname):
#         self.__name = name
#         self.__surname = surname
#
#     def __str__(self):
#         return self.__name+" "+self.__surname
#
# p1 = Person("Lady", "Gaga")
# print(p1)

# nums1 = [1, 6, 3, 4, 5, 6, 7, 8]
# nums2 = [1, 2, 3, 4, 2, 6, 7, 9]
#
# num_of_equal_pairs = sum(map(lambda i, j: j == i, nums1, nums2))
# print(num_of_equal_pairs)

# from collections.abc import Iterable
#
#
# lst = [1, 2, 3]
# lst2 = [5, 8, 4]
# m = map(lambda i, k: i+k, lst, lst2)
# print(*m)
# def map2(func, *seq):
#     try:
#         if not seq:
#             raise TypeError('map2() must have at least two arguments')
#         if not (isinstance(seq, Iterable)):
#             raise TypeError ('object is not iterable')
#         iters = [iter(s) for s in seq]
#         try:
#             while True:
#                 yield func(*[next(it) for it in iters])
#         except StopIteration:
#             pass
#     except TypeError as er:
#         print(er)
#
#
#
# result = map2(lambda i, k: i+k, [4,1], (6,8))
# print(*result)


class Parent:
    def present(self):
        return "I am a parent"

class Child(Parent):
    def present(self):
        print("I am a child")
        a = super().present()
        print("my parent said:", a)
c1 = Child()
c1.present()