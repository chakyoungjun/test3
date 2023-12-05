import streamlit as st
import numpy as np
import pandas as pd
import os
os.system('cls')
import sys
# sys.exit()

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

col1, col2 = st.columns([1, 2])
with col1:
    st.image('rabbit.jpg', width=300)
with col2:
    st.write('잡으면 후회할 인재(신수인💯, 시급3만원, 대박쩔어~~😆)')
    'Telephone📞 : 010 xxxx xxxx'
    'E-mail📧 : xxx1234@xxxxx.com'
    'Address🏠 : 충남 논산시 대학로 121'

''
''
col = st.columns(4)
with col[0]:
    st.link_button("Google(🌐)", "https://google.com")
with col[1]:
    st.link_button("Naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("Daum(🔎)", "https://daum.net")
with col[3]:
    st.link_button("Twitter(🐤)", "https://twitter.com")
''
''
'## :orange[자기소개]'
'#### 저는 시골에서 2남 1녀의 :red[가난한 집]의 장남으로 태어나...'


# fig, ax = plt.subplots()

# x = [-10, -9, -8, -7, -6]
# x

# x = []
# y = []
# for i in range(-10,11,1):
#     x.append(i)
#     y.append(3*i**3 - 5*i**2 + 3*i - 7)

# col1, col2, col3 = st.columns(3)

# with col1:
#     cc = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
# with col2:
#     ma = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p', 'h'])
# with col3:
#     ls = st.radio('선의 형태를 선택하시오', ['-', '--', '-.', ':',])

# plt.plot(x, y, '-.go')
# plt.plot(x, y, color=cc, linestyle=ls, marker=ma)
# st.pyplot(fig)
# fig, ax = plt.subplots()

# a = 2
# b = -5
# c = 3
# d = 7

# x = []
# y = []
# for i in range(-100, 101, 5):
#     x.append(i)
#     y.append(a*i**3 + b*i**2 + c*i + d)

# col1, col2, col3 = st.columns(3)
# with col1:
#     color = st.radio('색을 선택하시오', ('red', 'green', 'blue', 'gold', 'violet'))
# with col2:
#     linestyle = st.radio('선의 스타일을 선택하시오', ('-', '-.', ':'))
# with col3:
#     marker = st.radio('마커의 스타일을 선택하시오', ('s', 'o', '^'))

# if 'red' in color:
#     t = '-.r^'
# if 'green' in color:
#     t = '-.g^'
# if 'blue' in color:
#     t = '-.b^'

# plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)
# st.pyplot(fig)

# fig, ax = plt.subplots()

# arr = np.random.normal(1, 1, size=100)
# ax.hist(arr, bins=20)

# st.pyplot(fig)

# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')

# st.write('Hello, *World!* :sunglasses:')
# '# :rainbow[Hello], *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'
# '## Hello, *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'
# '### Hello, *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'
# '#### Hello, *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'
# '##### Hello, *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'
# '###### Hello, *World!* **tt** ***cc*** :red[red] :green[green] :blue[blue] 😎 🍻'


# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)


# list1 = list([['한빛', '남자', '20', '180'],
#               ['한결', '남자', '21', '177'],
#               ['김한결', '중성', '51', '155'],
#               ['한라', '여자', '20', '160']])
# n = np.array(list1)
# col_names = ['이름', '성별', '나이', '키']
# df = pd.DataFrame(list1, columns=col_names, index=['1행', '2행', '3행', '4행'])
# df


# genre = st.radio("선택하시오.", ["오름차순", "내림차순", "기타", '요약'],
#      horizontal=True, index=2)

# number = st.number_input('Insert a number', value=20, step=1)
# df.iloc[3, 2] = number

# if '오름' in genre:
#     st.dataframe(df.sort_values(by=['키']))
# if '내림' in genre:
#     st.dataframe(df.sort_values(by=['키'], ascending=False))
# if '기타' in genre:
#     st.dataframe(df)
# if '요약' in genre:
#     st.dataframe(df.describe())


# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li, index=['a', 'b', 'c', 'd'])
# li
# n
# p



# li = [1, 2, 3, 4]
# li

# for i in range(4):
#     li[i] = li[i] + 3
# li 

# li = np.array([1, 2, 3, 4])
# li + 30

# li = np.array([7, 2, 5, 4])
# li
# li_sort = np.sort(li)
# li_sort
# li_sort = np.sort(li)[::-1]
# li_sort

# for i in range(6):
#     r = random.randint(1, 45)
#     r


# t1 = turtle.Turtle()
# t1.shape('turtle')

# t1.width(5)
# t1.color('red')
# t1.penup()
# t1.goto(-100, 100)
# t1.pendown()
# t1.forward(100)

# t2 = turtle.Turtle()
# # t2.shape('turtle')

# t2.width(5)
# t2.color('blue')
# t2.penup()
# t2.goto(-100, -100)
# t2.pendown()
# t2.forward(100)

# for i in range(30):
#     d1 = random.randint(1, 60)
#     t1.forward(d1)
#     d2 = random.randint(1, 60)
#     t2.forward(d2)


# turtle.done()

# a = np.array([1, 10, 5, 2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(a**0.5)
# print(np.square(a))
# print(a**2)


# a = np.arange(8)
# a
# a.shape = (4, 2)
# a
# b = a.flatten()
# b
# b.resize((2, 4))
# b
# c = np.resize(b, (2, 4))
# c

# n = 100
# for i in range(1, n+1):
#     if i%7 == 3:
#         i


# n = 7
# arr = np.full((n, n), '나머지')
# arr

# for i in range(n):
#     for j in range(n):
#         # arr[i, j] = '나머지'
#         if i == j or i + j == n-1:
#             arr[i, j] = '대'
#         # if i + j == n-1:
#         #     arr[i, j] = '대'

# arr


# n = np.full((4, 5), 10)
# n

# n1 = np.zeros((4, 5))
# n1
# for i in range(4):
#     for j in range(5):
#         n1[i, j] = 10
# n1

# n2 = []
# n2.append(10)
# n2
# n2 = np.append(n2, 15)
# n2

# arr = np.array([1, 2, 3])
# s = arr.sum()
# s
# s1 = np.sum(arr)
# s1

# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]
# for i in range(4):
#     list1[i] = list1[i] + 3

# list1

# a = np.array(list1)
# a

# a.ndim
# n = np.ndim(a)
# np.size(a)
# a.size
# a.shape
# a.T


# a.shape
# s = a.sum(axis=0)
# s
# mn = a.min(axis=0)
# mn
# mx = a.max(axis=0)
# mx

# a = np.zeros(2)
# a
# b = np.zeros((2,2))
# b
# c = np.ones((2,3))
# c
# d= np.full((2,3), 5)
# d
# e = np.eye(5)
# e

# list1 = ([[10,10,10,10,10,10],[10,10,10,10,10,10],[10,10,10,10,10,10],[10,10,10,10,10,10],[10,10,10,10,10,10]])
# a = np.array(list1)
# a
 

# def user_eye(n):
#     arr = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == n-j-1:
#                 arr[i, j] = 1
#     return arr

# arr = user_eye(10)
# arr


# t = turtle.Turtle()
# t.shape('turtle')
# t.write("차", move=False, align="center", font=("arial",50,"bold"))

# t.penup()
# t.sety(-100)
# t.pendown()


# turtle.done()

# print('dfa
# sdfasd 파이썬')
# st.write('dfasdfasd 파이썬')
# r = 15
# Area = 3.14*r*r
# Area
# st.write(Area)

# a = 11
# b = 4

# a > b
# a < b
# t1 = a == b
# t2 = a != b

# grade = 72
# if grade >= 90:
#     'A'
# elif grade >= 80:
#     'B'
# elif grade >= 70:
#     'C'
# elif grade >= 60:
#     'D'
# else:
#     'F'

# 'a' + 'bcd' + str(5)

# for a in range(2,10):
#     ''
#     a, '단입니다'
#     for i in range(1,10,1):
#         b = str(a) + 'X' + str(i) + '=' + str(a*i) 
#         b

# li = [1, 2, 3, 4, 5, 1, 3]
# li
# a = len(li)
# a
# li[-2]
# li.append(100)
# li
# c = li.count(0)
# c

# li.sort(reverse=True)
# li

# dict = {'name':'신수인', 'weight':69, 'height':172, 'address':'충남 논산로 대학로 121', 'hobby':'게임,독서'}
# dict['family'] = ['아빠', '엄마', '여동생']
# dict['hobby'] = ['축구, 등산']
# del dict['hobby']
# del dict['family']
# dict
# for k in dict.keys():
#     k
# for v in dict.values():
#     v
# '========================================='
# for k, v in dict.items():
#     k
#     v
# ty = type(dict)
# ty

# s = 0
# for i in range(1, 1000+1,):
#     s = s + i

# s


# list_1 = [1, 2, 7, 4, 50, 33,]
# mx = max(list_1)
# mn = min(list_1)
# s = sum(list_1)
# s, mx, mn



# def sta(arr):
#     s = 0
#     mx = -1e10
#     mn = 1e10
#     for i in arr:
#         s = s + i
#         if mx < i:
#             mx = i
#         if mn > i:
#             mn = i
#     arr
#     'sum = ', s, 'mn = ', mn, 'mx = ', mx
#     return s, mx, mn


# list_1 = [5, 13, 7, 4, 11]
# [s1, mx1, mn1] = sta(list_1)
# s1, mx1, mn1

# def numbers(n):
#     for i in range(1, n):
#         if i % 7 == 3:
#             i
# a = numbers(20)
# a







