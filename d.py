# coding = utf-8
# @Time: 2021/6/3 20:03
# @Author: 任添宁
# @File: d.py
# @Software: PyCharm
import time

def calculate(f):   #f用来做回调的函数
    def wrapper():
        start = time.time()
        print("开始时间：{}".format(start))
        f()
        end = time.time()
        print("结束时间：{}".format(end))
        sum = end - start
        print("执行的时间是：{}".format(sum))
    return wrapper  #返回函数wrapper，这个wrapper函数回调了传进来的f，并在回调前后加了三条语句。

@calculate
def fn():
    print("开始执行")
    time.sleep(1)   #这里相当于 fn = calculate(fn) 把fn函数作为参数传入另一个函数，然后回调。并且decorator的返回值赋值给了fn

fn()