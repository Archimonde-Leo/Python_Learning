'''
定义一个学生类，描述学生
'''
# 定义一个空类
class Student():
    # pass代表跳过
    pass

# 定义一个对象
mingyue = Student()

# 定义一个听课的学生类
class PythonStudent():
    name = None
    age = 18
    course = 'Python'
    # 注意函数的缩进
    def doHomework(self):
        print("I 在做作业")

        return None

# 实例化
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 函数没有传参
yueyue.doHomework()