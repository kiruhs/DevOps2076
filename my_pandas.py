from time import sleep
import pandas as pd
import numpy as np
# from numpy.conftest import dtype
from tabulate import tabulate
import matplotlib
import matplotlib.pyplot as plt

# ls = [1, -3, 6]
# print(ls)
# series = pd.Series(ls,index=['a', 'b', 'c'], dtype=np.int16)
# print(series)

# ls2 = ['100', 'python', '3001.21', '230', '400']
# ser2 = pd.Series(ls2)
# # print(ser2)
# print("Change the original series to numeric")
# ser3 = pd.to_numeric(ser2, errors='coerce')
# # print(ser3)
# sort_s = ser3.sort_values()
# print(sort_s)
# print(sort_s[2])

# calories = {'day1': 420, 'day2':380, 'day3': 395}
# mycal = pd.Series(calories, index=['day1', 'day3'])
# print(mycal)

# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series([2, 4, 6, 8, 10])

# print("Items of s1 that are not presented in s2")
# result = s1[~s1.isin(s2)]
# print(result)

# s11 = pd.Series(np.union1d(s1, s2))
# print(s11)
# s22 = pd.Series(np.intersect1d(s1, s2))
# print(s22)
# print("Items that are not common of two given series")
# result = s11[ ~s11.isin(s22)]
# print(result)

# DataFrame - 2D

# df = pd.DataFrame([[1, 'John', 5.0], [2, 'Mary', 4.8], [3, 'Bob', 4.3]], columns=['#', 'Name', 'Score'], index=['a','b','c'])
# data = {'calories': [420,40, 45, 47, 55]}

# df = pd.DataFrame(data, index=['day1', 'day2', 'day3', 'day4', 'day5'])
# print(df)

# print(df['calories'])
# print(df.loc[1])
# print(df.iloc[[1, 3]])
# print(df.iloc[[-1]])
# print(df.loc[['day3']])

# url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
# tbl = pd.read_html(url, encoding='utf8')
# csv_tbl = tbl[1].to_csv('gdp.csv', encoding='utf8', index=True)
# sleep(2)
# new_tbl = pd.read_csv('gdp.csv', encoding='utf8')
# print(new_tbl.to_string())
# print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
# print(new_tbl.info())
# print(new_tbl.head(10))
# print(new_tbl.iloc[-1])
# dct = new_tbl.to_dict()
# print(dct)
# print(new_tbl['Country/Territory'])
# df = new_tbl.dropna()
# print(df.to_string())
# new_tbl.dropna(inplace=True)
# print(new_tbl.to_string())
# print(df)

# print(new_tbl["Country/Territory"].iloc[3])
# new_tbl.iloc[3,1] = "Israel"
# print(new_tbl.to_string())


# df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'c', 'd'])
# print(df)
# df.drop(columns=['b', 'c'], inplace=True)
# print(df.drop(columns=['b', 'c']))

# print(df.drop(['b', 'c'], axis=1))
# print(df.drop([0, 1], axis=0))
# print(df.drop(index=[0, 1]))

# df = pd.DataFrame( { 'X': [100, 100, 100, 80, 90, 90, 100],
#                      'Y': ['Alex', 'Jane', 'Sweta', 'Andrey', 'Elena', 'Gleb', 'Gregory'],
#                      'Z': [22234, 24230, 1342348, 2234230, 123423, 12340, 43240]
#                   } )
# print(df)
# print(df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist()))

# df = pd.DataFrame( {
#     'id': [1, 1, 2, 3, 3, 4, 4, 4],
#     'value': ['a', 'a', 'b', None, 'a', 'a', None, 'b']
# })
# print(df)
# print(df.groupby('value')['id'].nunique())

# df = pd.DataFrame({
#     'book_name': ['Book1', 'Book2','Book3', 'Book4', 'Book1', 'Book2', 'Book3', 'Book5'],
#     'book_type': ['Math', 'Physics', 'Computer', 'Science', 'Math', 'Physics', 'Computer', 'English'],
#     'book_id': [1, 2, 3, 4, 1, 2, 3, 5]
# })
# print(df)
#
# result = df.groupby(['book_name', 'book_type'])['book_type'].count().reset_index(name="count")
# print(result)

# df = pd.DataFrame({
#     'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
#     'purchase_amt': [150.5, 270.65, 65.26, 100.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
#     'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'],
#     'customer_id': ['C3001', 'C3001', 'D3005', 'D3001', 'C3005', 'D3001', 'C3005', 'D3001', 'D3005', 'C3001', 'D3005', 'D3305'],
#     'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
# })
# print(df)
# print("=============================================")
# split the Dataset into groups on salesman and calculate the number of customers starting with 'C', the list of
# all products and the difference between maximum purchase and minimum purchase amount

# def customer_id_C(x):
#     return (x.str[0] == 'C').sum()
#
# result = df.groupby(['salesman_id']).agg(customer_id_C = ('customer_id', customer_id_C),
#                                          customer_id_list = ('customer_id', lambda x: ', '.join(x)),
#                                          purchase_amt_gap = ('purchase_amt', lambda x: x.max()-x.min()),
#                                          customer_id_C_list = ('customer_id', lambda x: ', '.join(name for name in x if name.startswith('C')))
#                                          )
#
# print(result.to_string())

# df = pd.DataFrame({
#     'student_id': ['S001', 'S001', 'S002', 'S002', 'S003', 'S003'],
#     'marks': [[88,89,90], [78,81,60], [84,83,91], [84, 88,91], [90,89,92], [88,59,90]]
# })
#
# print(df)
# print("=======================")
# result = df.set_index('student_id')['marks'].groupby('student_id').apply(list).apply(lambda x: np.mean(x, 0))
# print(result)

df = pd.read_csv('test.csv', encoding='utf-8')
# print(df.dropna().loc[0,'col7'])
# print(df.dropna().loc[2:,'col7'])
df['col7'] = df.loc[2:]['col7'].str.replace(',', '')
df['col6'] = df.loc[2:]['col6'].str.replace(',', '')
df['col4'] = df.loc[2:]['col4'].str.replace(',', '')
head = df.iloc[0]
df.dropna(inplace=True)
# print(df.col7)
df.col7 = df.col7.str.strip('"').astype(float)
df.col6 = df.col6.str.strip('"').astype(float)
df.col4 = df.col4.str.strip('"').astype(float)

df1 = df.loc[2:][df.loc[2:, 'col7'] < 3000]
# print(tabulate(df1, headers=head, tablefmt='psql'))
df1.col5 = df1.col5.str.strip('%').astype(float)/100
# print(df1.col5.mean())
# print(df1.col7.sum())
# print(df1.col4.max())

# print(df1.groupby('col4').col7.sum())
# print(df1.groupby('col4').col7.mean())
# print(df1.groupby('col4').col7.std())
# df1.col6.plot()
# df1.col7.plot()
#
# plt.savefig("stocks.png")
# plt.show()

# class MyDF(pd.DataFrame):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for col in self.columns:
#             self[col] = self[col].str.replace('+', '')
#             self[col] = self[col].str.replace('2 5', '25')
#             self[col] = pd.to_numeric(self[col], errors='ignore')

# df = pd.read_csv('data.csv', encoding='utf-8')
# data = MyDF(df)
# print(data)
# print(type(df.loc[2,'phone']))
# print(type(data.loc[2,'phone']))
# df = df.sort_values([df.columns[0], df.columns[1]], ascending=False)
# print(df)

# w_a_con = pd.read_csv("world_alcohol.csv")
# # print(w_a_con.to_string())
# # print(w_a_con.sample(5))
# # print(w_a_con.sample(frac=0.1))
# # print(w_a_con.drop_duplicates("WHO region").drop_duplicates("Beverage Types"))
# print(w_a_con[w_a_con["Country"] == "Norway"])


# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
#     'C': [7, 8, 9]
# })
#
# def square(x):
#     return x**2
# # print("Original")
# # print(df)
# print("Squared")
# df_sq = df.map(square)
# print(df_sq)
#
# df_trans = df_sq.T
# print(df_trans)
#
# df_clock_wise = df_sq[::-1].T
# print(df_clock_wise)
#
# df_counter_clock_wise = df_sq.T[::-1]
# print(df_counter_clock_wise)

# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6]
# })
# using iterrows (for method)
# for index, row in df.iterrows():
#     df.at[index, 'C'] = row['A'] + row['B']
# df['C'] = df['C'].astype(int)
# print(df)

# using apply
# df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
# print(df)

# Vectorize

# df['C'] = df['A'] + df['B']
# print(df)

import timeit

df = pd.DataFrame({'A': np.random.randint(1, 100, 100000),
                   'B': np.random.randint(1, 100, 100000)})

def iterrows_add():
    for index, row in df.iterrows():
        df.at[index, 'C'] = row['A'] + row['B']

def apply_add():
    df['C'] = df.apply(lambda row: row['A'] + row['B'], axis=1)

def vector_add():
    df['C'] = df['A'] + df['B']

vect_time = timeit.timeit(vector_add, number=1)
iterrows_time = timeit.timeit(iterrows_add, number=1)
apply_time = timeit.timeit(apply_add, number=1)

print(f"Vectorized time: {vect_time}")
print(f"Iterrows time: {iterrows_time}")
print(f"Apply time: {apply_time}")

