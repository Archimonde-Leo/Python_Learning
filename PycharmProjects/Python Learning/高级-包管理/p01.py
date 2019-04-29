# 包含一个学生类
# 一个sayHello函数
# 一个打印语句

class Student():
    def __init__(self, name = "NoName", age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi,欢迎来到NUAA")

print("我是模块p01，有何贵干？")