# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/8 0008 23:58
# @Author   : Gpp
# @File     : test_for_process_thread.py
import threading, time

# def a_thread():
#     print('i am a thread')
#     # time.sleep(3)
#     print(threading.current_thread().getName())
#
#
# t = threading.Thread(target=a_thread)
# t.start()
# print(threading.current_thread().getName())


# 线程隔离
# 操作数据
# werkzug local local 字典

# {thread——id1：}
from werkzeug.local import Local


class A:
    b = 1


# my_obj = A()
my_obj = Local()
my_obj.b = 1


def worker():
    # 新线程
    time.sleep(2)
    my_obj.b = 2
    print('in new thread b is:' + str(my_obj.b))


new_t = threading.Thread(target=worker)
new_t.start()
# time.sleep(1)

print('in main thread b is:' + str(my_obj.b))
