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
        - 案例p04.py