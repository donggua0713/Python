# import time
#
# # print(time.time())
# # #显示自1970年到现在的秒数
# #
# # print(time.localtime(time.time()))
# # print(time.localtime(time.time()).tm_year)
# # #(结构化时间，后面可以跟上：tm_year=2018, tm_mon=1, tm_mday=2, tm_hour=22, tm_min=0, tm_sec=20, tm_wday=1, tm_yday=2, tm_isdst=0)
# #
# # print(time.asctime(time.localtime(time.time())))
# # #获取简单的可读的时间：Tue Jan  2 22:02:00 2018
# #
# # print(time.strftime("%Y-%M-%d",time.localtime(time.time())))
# # print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time())))
# # #格式化时间：2018-03-02 ，
# #
# #
# # print(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
# # #把一个格式化后的字符串，转换成struct_time格式
# #
#
# a = time.asctime(time.localtime(time.time()))
# print(time.time())
# print(a)
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# #mktime， 把struct_time的格式时间，转换成秒的格式
#
#

import calendar
cal=calendar.month(2018,1)
print(cal)