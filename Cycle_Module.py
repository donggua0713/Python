import os,stat,re

# i=1
# 常规的while，后面跟上判断条件，如果成立则继续。break用于跳出整个循环，continue用于跳出当次循环
#
# while os.getcwd() == 'C:\\Users\\dongdong.yu\\Documents\\PycharmProjects\\Python':
#     print('yes')
#     break



# 设置一个常量在while后面，表示一定会成立，后续再控制何时跳出
#
# while 1:
#     print(os.getcwd())
#     i += 1
#     if i > 10:
#         break



#while可以用else来表示false的动作
# while i <= 10:
#     print('yes')
#     i=i+1
# else:
#     print('no')

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# import random
# import sys
# import time
#
# result = []
# while True:
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     print(result)
#     count = 0
#     index = 2
#     pointStr = ""
#     while index >= 0:
#         currPoint = result[index]
#         count += currPoint
#         index -= 1
#         pointStr += " "
#         pointStr += str(currPoint)
#     if count <= 11:
#         sys.stdout.write(pointStr + " -> " + "小" + "\n")
#         time.sleep( 1 )   # 睡眠一秒
#     else:
#         sys.stdout.write(pointStr + " -> " + "大" + "\n")
#         time.sleep( 1 )   # 睡眠一秒
#     result = []


# i = 1
# while i:
#     j = 1
#     while j:
#         print(j, "*", i, " = ", i * j, '  ')
#         if i == j:
#             break
#
#         j += 1
#         if j >= 10:
#             break
#
#     print( "\n" )
#     i += 1
#     if i >= 10:
#         break


# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):             #此时index取值为len的值0 1 2 ， 则这样循环3次
#     print( '当前水果 :', fruits[index])
#
# print("Good bye!")

# fruits = ['banana', 'apple', 'mango']
# for sg in fruits:
#     print(sg)


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')

# for i in range(2,4):
#     print(i)


#外边一层循环控制行数
#i是行数
# i=1
# while i<=9:
#      #里面一层循环控制每一行中的列数
#      j=1
#      while j<=i:
#           mut =j*i
#           print("%d*%d=%d"%(j,i,mut), end="  ")
#           j+=1
#      print()
#      i+=1

#
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print('%d*%d=%d' % (j,i,i*j),end="\t")
#         j+=1
#     i+=1
#     print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         # if j <= i:
#         print('%d*%d=%d' % (j, i, i * j), end="  ")
#         j += 1
#     print()

# i=2

# susu=[];
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         susu.append(i)
# print(susu)




# susu=[]
# i=2
# j=2
# while i<100:
#     j=2
#     while j<i:
#         if i%j == 0:
#             break
#         j+=1
#     else:
#         susu.append(i)
#     i+=1
# print(susu)



# susu=[]
# i=30
# while i in range(30,101):
#     j=2
#     while j in range(2,i):
#         if i%j==0:
#             break
#         j+=1
#     else:
#         susu.append(i)
#     i+=1
# print(susu)


#!/usr/bin/python
# -*- coding: UTF-8 -*-

#*字塔
# i=1
# while i<=9:
#     if i<=5:
#         print("@"*i)
#     elif i>5 and i<=9:
#         print("@"*(10-i))
#     i+=1
#
#
# for i in range(10):
#     if i<=5:
#         print('$'*i)
#     elif i>5 and i<10:
#         print('$'*(10-i))


# array = [9,2,7,4,5,6,3,8,1,10]
# L = len(array)
# for i in range(L):
#     for j in range(L-i):
#         if array[L-j-1]<array[L-j-2]:
#             array[L-j-1],array[L-j-2]=array[L-j-2],array[L-j-1]
# print(array)
#
# array = [9,2,7,4,5,6,3,8,1,10]
# j=0
# while j in range(len(array)):
#     i=0
#     while i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             # array[i],array[i+1]=array[i+1],array[i]
#             total=array[i] + array[i+1]
#             array[i]=total - array[i]
#             array[i+1]=total - array[i]
#         i+=1
#     j+=1
# print(array)
#
#


# array = [9,2,7,4,5,6,3,8,1,10]
# for i in range(len(array)):
#     for j in range(len(array)-1):
#         if array[j] > array[j+1]:
#             array[j],array[j+1]=array[j+1],array[j]
#         j+=1
#     i+=1
# print(array)

# for i in range(11):
#     if i%2==0:
#         continue
#     print(i)
# print(i)

# if 'txt' in (os.listdir('C:\\')):
#     print('yes')
# else:
#     print('no')

# for x in (os.listdir('C:\\')):
#     print(x)
#     print(x.count('o'))

# x=['c','ab','ac']
# x.append('d')
# print(x)


aList = ['123', 'xyz', 'zara', 'abc'];

# print("A List : ", aList.pop())
# print(aList)
# print("B List : ", aList.pop(2))
# print(aList)


aList.reverse()
print(aList)
aList.sort()
print(aList)