#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类
class Student():

    # 类的初始化方法
    def __init__(self ,name ,score):
        # 属性
        self.name = name
        self.score = score
    # 方法 函数
    def description(self):
        print(self.name +"'s score is :"+ str(self.score))



if __name__=="__main__":

    # s0 为 Student类的对象
    s0 = Student("tom",90)
    s1 = Student("sunny",80)
    s3 = Student("jerry",70)
    s_list = [s0 ,s1 ,s3]
    # 循环
    for i in s_list:
        i.description()









