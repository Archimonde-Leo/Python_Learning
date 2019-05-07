'''
利用time函数，生成两个函数
多线程调用
计算总的运行时间
带参数多线程启动
'''
import time
import threading

def loop1(in1):
    print('Start loop1 at:', time.ctime())
    print("我是参数", in1)
    time.sleep(4)
    print('End loop1 at:', time.ctime())

def loop2(in1, in2):
    print('Start loop2 at:', time.ctime())
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def main():
    print('Starting at:', time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("yty", ))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("yty", "zr"))
    t2.start()

    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 启动多线程后本线程作为主线程存在
    # 若主线程执行完毕，子线程可能会被中止
    while True:
        time.sleep(10)