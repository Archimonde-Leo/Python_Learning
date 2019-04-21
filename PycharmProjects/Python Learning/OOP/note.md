# 0.OOP-Python 面向对象
- Python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合
- 魔法函数
    - 魔法函数概述
    - 构建类魔法函数
    - 运算类魔法函数
    
# 1.面向对象概述（ObjectOriented,OO）
- OOP思想
    - 对于任何一个任务，考虑任务环境中的各个模型
- 几个名词
    - OO：面向对象
    - OOA：面向对象分析
    - OOD：面向对象设计    
- 类和对象的概念
    - 类：具有共性的事物组成的集合
    - 对象：具象的事物，个体
    - 类跟对象的关系
        - 一个具象，一个抽象
- 类中的内容
    - 属性（变量）：事物的特征
    - 成员方法（函数）：事物功能或动作

# 2.类的基本实现
- 类的命名
    - 大驼峰（每个单词首字母大写，多个单词直接相连）
    - 避开关键字或系统命名相似的命名
- 声明一个类
    - class关键字
    - 仅有属性和成员方法
    - 案例 01.py
- 实例化类

        变量 = 类名（）
- 访问成员对象
    - 使用点操作符
    
            obj.成员属性名称
            obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
    
            # dict前后各有两个下划线
            obj._ dict_
    - 类所有的成员
    
            # dict前后各有两个下划线
            classname._dict_
            
# 3.anaconda基本使用
- anaconda主要是一个虚拟环境管理器，此外还是一个安装包管理器
- conda list：显示anaconda安装的包
- conda env list：显示anaconda的虚拟环境列表
- conda create -n xxx python=3.7：创建python版本3.7的虚拟环境，名为xxx
        
        若下载时出现网络问题，可使用清华镜像源，
        方法见https://blog.csdn.net/JessieLiu_/article/details/80112278
- conda activate xxx：激活xxx环境
- conda deactivate：脱离当前环境
- 查看所有虚拟环境所在目录：conda info --envs

# 


    