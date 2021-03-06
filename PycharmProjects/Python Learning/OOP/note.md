# 0.OOP-Python面向对象
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
            obj.__dict__
    - 类所有的成员
    
            # dict前后各有两个下划线
            classname.__dict__
            
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

# 4.类和对象的成员分析
- 类和对象都可以存储成员，某个成员可以归属于类，也可以归属于对象
- 类存储成员时使用的是与类关联的一个对象
- 对象存储成员是存储在当前对象中
- 对象访问一个成员时，若找不到该成员，尝试访问类中的同名成员
                  若找到该成员，一定使用对象中的成员
- 创建对象时，类中成员不会放入对象中，而是得到一个空对象，没有成员
    - 案例02.py
- 通过对象对类中成员赋值或对象添加成员时，对应成员会保存在对象中，而不会修改类成员

# 5.关于self
- self在对象方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入当前方法的第一个参数中
- self不是关键字，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法称为非绑定类的方法，可以通过对象访问
  没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名的方式来访问

# 6.面向对象的三大特性
- 封装
- 继承
- 多态

## 6.1 封装
- 封装即对对象成员进行访问限制
- 封装三个级别：
    - 公开：public
    - 受保护的：protected
    - 私有的：private
    - public，private，protected都不是关键字
- 判别对象位置
    - 对象内部
    - 对象外部
    - 子类
- 私有 private
    - 私有成员是最高级别封装，只能在当前类或对象中访问
    - 在成员前添加两个下划线
    
            class Person():
                # name是共有成员
                name = "yty"
                # __age是私有成员
                __age = 18
    - Python的私有与C++不同，是一种称为name mangling的改名策略，
    可以使用对象._classname_attributename访问
- 受保护的封装 protected
    - 将成员对象进行一定级别的封装，在类中或子类中都可以访问，但在外部不行
    - 在成员前添加一个下划线
- 公开的封装 public
    - 对成员没有任何操作，任何方法都可以访问
- [下划线作用](https://blog.csdn.net/tcx1992/article/details/80105645)
    
## 6.2 继承
- 继承就是一个类可以获得另外一个类中的成员属性和成员方法
- 作用：减少代码，增加代码的复用功能同时可以设置类与类直接的关系
- 继承与被继承的概念
    - 被继承的类叫父类，也叫基类
    - 用于继承的类，叫子类，也叫派生类
    - 继承与被继承一定存在一个is-a关系
- 继承的语法，见02.py
- 继承的特征
    - 所有类继承自object类
    - 子类可以使用父类中除私有成员外的所有内容
    - 子类继承父类并没有将父类成员赋值到子类，而是通过引用关系访问调用
    - 子类中可以定义独有的成员属性和方法
    - 子类中若定义与父类中相同的成员，优先使用类中成员
    - 子类若想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码复用，
    可以使用 父类名.父类成员 的格式来调用父类成员，也可以使用 super().父类成员 的格式来调用
- 继承变量函数的查找顺序问题
    - 优先查找自己的变量
    - 没有则查找父类
    - 构造函数若本类没有定义，则自动查找调用父类构造函数
    - 如果本类有定义，则不再继续向上查找
- 构造函数
    - 是一类特殊的函数，在类实例化之前进行调用
    - 如果定义了构造函数，实例化时只用自己的
    - 没有定义，则自动向上查找父类构造函数
    - 如果子类没定义，父类构造函数带参数，则构造对象时的参数应该按父类参数构造
- super
    - super不是一个关键字，而是一个类
    - super的作用是获取MRO（MethodResolustOrder）列表中的第一个类，往往是父类
    - super与父类没有实质性联系
    - super使用两个方法，参见在构造函数中调用父类的构造函数
    
- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
    
- 单继承和多继承的优缺点
    - 单继承：
        - 传承有序 逻辑清晰 语法简单
        - 功能不能无限扩展，只能在当前唯一继承链中拓展
    - 多继承
        - 优点：类的功能拓展方便
        - 缺点：继承关系混乱

- 菱形继承/钻石继承问题
    - 多个子类继承自同一父类，这些子类被同一个类继承，于是继承关系图形成一个菱形图谱
    - [MRO](https://www.cnblogs.com/whatisfantasy/p/6046991.html)
    - 关于多继承的MRO
        - MRO就是多继承中，用于保存继承顺序的一个列表
        - python本身采用C3算法来对菱形继承进行计算的结果
        - MRO列表的计算原则：
            - 子类永远在父类前面
            - 多个父类根据继承语法中括号内书写的顺序存放
            - 多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一个父类的父类

## 6.3 多态
- 多态就是一个对象在不同情况下以不同的状态出现
- 多态在python中不是语法，是一种思想
- 多态性：一种调用方式，不同执行效果
- 多态：同一事物的多种形态
- [多态和多态性](https://www.cnblogs.com/luchuangao/p/6739557.html)

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行拓展
    
- 我们使用多继承语法来实现Mixin
- 使用Mixin实现多继承要非常小心
    - 首先它必须表示某单一功能而不是物品
    - 职责必须单一，如果需要多个功能，可以写多个Mixin
    - Mixin不能依赖于子类的实现
    - 子类即使没有继承这个Mixin类，也能照样工作，只是缺少莫个功能
- 优点
    - 可以在不对类进行任何修改的情况下扩充功能（模块化思想）
    - 可以方便组织与维护不同功能组件
    - 可以根据需要调整功能类组合
    -避免创建很多新类，导致类的继承混乱
    
# 7.类相关函数
- issubclass：检测一个类是否是另一个类的子类
- isinstance：检测一个对象是否是一个类实例 
- hasattr: 检测一个对象是否有成员xxx
- getattr:get attribute
- setattr:set attribute
- delattr:delete attribute
- dir:获取对象成员列表

# 8.类的成员描述符(属性)
- 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
    - get:获取属性的操作
    - set:修改或添加属性
    - delete:删除属性
- 三种使用方法
    - 使用类实现描述器
    - 使用属性修饰符
    - 使用property函数
        - property函数很简单
        - property(fget,fset,fdel,doc)
    - 案例见02.py
- 无论哪种修饰符都是为了对成员属性进行相应的控制，区别在于
    - 类的方式：适合多个类中的多个属性共用一个描述符
    - property：当前类中使用，可以控制一个类中多个属性
    - 属性修饰符：当前类中使用，控制一个类中的某一属性

# 9.类的内置属性

        __dict__:以字典的方式显示类的成员组成
        __doc__:获取类的文档信息
        __name__:获取类的名称，在模块中使用可获取模块名
        __bases__:获取某个类的所有父类，以元组的方式显示
        
# 10.类的常用魔术方法
- 魔术方法就是不需要人为调用的方法，基本在特定的时刻自动触发
- 魔术方法的统一特征：方法名被前后各两个下划线所包裹
- 操作类
    - `__new__`:对象实例化方法，此函数较特殊，一般不需要使用
    - `__init__`:构造函数
    - `__call__`:对象当函数使用时来触发
    - `__str__`:对象当字符串使用时来调用
    - `__repr__`:返回字符串，与`__str__`有区别
- 描述符相关
    - `__set__`
    - `__get__`
    - `__delete__`
- 属性操作相关
    - `__getattr__`:访问不存在属性时触发
    - `__setattr__`:对成员属性进行设置时触发
        - 参数：self用来获取当前对象
        - 被设置的属性名称以字符串形式出现
        - 需要对属性名称设计的值
    - 作用：进行属性设置时进行验证或修改
    - 注意：该方法中不能对属性直接赋值，否则死循环
    - 参看案例
- 运算分类相关魔术方法
    - `__gt__`:进行大于判断时触发的函数
        - 参数：
            - self
            - 第二个参数是第二个对象
            - 返回值可以是任意值，推荐返回布尔值
            - 参看案例
            
# 11.类和对象的三种方法
- 实例方法
    - 需要实例化对象才能采用的方法，使用过程中可能需要截止对象的其他对象的方法完成
- 静态方法
    - 不需要实例化，通过类直接访问
- 类方法
    - 不需要实例化
- 三种方法内存使用方面有区别

# 12.抽象类
- 抽象方法：没有具体实现内容的方法称为抽象方法
- 主要意义是规范了子类的行为和接口
- 抽象类的使用需要借助abc模块

        import abc
        
- 抽象类：包含抽象方法的类，通常称为ABC
- 抽象类的使用
    - 抽象类中可以包含抽象方法，也可以包含具体方法
    - 抽象类中可以有方法也可以有属性
    - 抽象类不允许直接实例化
    - 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
    - 假定子类没有实现所有继承的抽象方法，则子类也不能实例化
    - 抽象类的主要作用是设定类的标准，以便开发时有统一规范
    
# 13.自定义类
- 类其实是一个类定义和各种方法的自由组合
- 可以定义类和函数，然后通过类直接赋值
- 可以定义类和函数，然后借助于MethodType实现
- 借助于type实现
- 利用元素实现-MetaClass
    - 元类是类
    - 作用是创造别的类
