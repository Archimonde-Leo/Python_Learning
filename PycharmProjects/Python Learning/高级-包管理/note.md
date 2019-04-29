# 1.模块
- 一个模块就是一个包含python代码的文件，后缀名为.py，模块就是个python文件
- 为什么用模块
    - 功能拆分
    - 代码复用
    - 避免命名冲突，当作命名空间使用
- 如何定义模块
    -模块就是个普通文件，可以直接写
    - 根据规范，应当编写以下内容
        - 函数（功能单一）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
        
- 如何使用模块
    - 模块直接导入
        - 加入模块名称不能以数字开头，因为python中变量不能以数字开头
        - 要导入以数字开头的模块，可借助于importlib包，案例见01.py 02.py
        - 语法
    
                import module_name
                module_name.function_name
                module_name.class_name
                
        - 案例见p01.py p02.py        
    - import 模块 as 别名
        - 导入的同时给模块一个别名
        - 其余用法跟第一种相同
        - 案例p03.py
    - from module_name import func_name, class_name
        - 按上述方法有选择性地导入
        - 使用时可以直接使用导入的内容，不需要前缀
        - 案例p04.py
    - from module_name import *
        - 导入模块所有内容
        - 案例p05.py
        
- `if __name__ == "__main__"`的使用
    - 可以有效避免模块代码被导入时被动执行的问题
    - 建议所有程序以此代码作为程序入口
    
# 2.模块的搜索路径与存储
- 模块搜索路径：
    - 加载模块时，系统会在哪些地方寻找此模块
- 系统默认模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
        案例p06.py
        
- 添加搜索路径
        
        sys.path.append(dir)
        
- 模块的加载顺序
    1.搜索内存中已经加载好的模块
    2.搜索python的内置模块
    3.搜索sys.path
    
# 3.包
- 包是一种组织管理代码的方式，包里面存放着模块
- 用于将模块包含在一起的文件夹
- 自定义包的结构

        /---包
        /---/--- __init__.py 包的标志文件
        /---/--- 模块1
        /---/--- 模块2
        /---/--- 子包
        /---/---/--- __init__.py 包的标志文件
        /---/---/--- 子包模块1
        /---/---/--- 子包模块2
        
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容（实际情况下往往没有内容）
        - 使用方式是：
        
                package_name.func_name
                package_name.class_name.func_name()
                
        - 此种方式的访问内容是
        - 案例 pkg01, p07.py
    - import package_name as p
        - 具体用法和作用方式跟上述简单导入一致
        - 注意的是此种方法是默认对__init__.py内容的导入
    - import package.module
        - 导入包中某个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func()
                package.module.class.var
                
        - 案例 p08.py        
    - import package.module as pm
    - from ... import 导入
        - from package import module1, module2, ...
        - 此种导入方法不执行__init__.py的内容
        
                from pkg01 import p01
                p01.func()
        - from package import *
            - 导入当前包__init__.py文件中所有的函数和类
            - 使用方法
            
                    func_name()
                    class_name.func_name()
                    class_name.var
                    
            案例 p09.py,注意此种导入的具体内容
    - from package.module import *
        - 导入包中指定的模块的所有内容
        - 使用方法
            
                func_name()
                class_name.func_name()
                
    - 在开发环境中会经常使用其它模块，可以在当前包中直接导入其它模块中的内容
        - import 完整的包或者模块的路径
    - `__all__`的用法
        - 在使用from package import * 的时候，* 可以导入的内容
        - `__init__.py`中如果文件为空，或者没有`__all__`，那么只可以导入`__init__.py`的内容
        - `__init__.py`如果设置了 `__all__`的值，那么按照`__all__`指定的子包或模块进行加载，
        如此则不会载入__init__.py`的内容
        - `__all__ = ['module1', 'module2', 'package1'...]`
        
# 4.命名空间
- 用于区分不同位置不同功能但名称相同的函数或变量的特定前缀
- 作用是防止命名冲突

        setName()
        Student.setName()
        Dog.setName()