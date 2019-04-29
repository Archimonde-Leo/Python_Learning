# 借助于importlib包可以实现导入以数字开头的模块
import importlib

# 相当于导入了一个叫01的模块并把导入模块值给了p01
p01 = importlib.import_module("01")

stu = p01.Student("yty", 19)

stu.say()

p01.sayHello()