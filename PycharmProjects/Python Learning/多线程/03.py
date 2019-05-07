'''
利用time函数，生成两个函数
多线程调用
计算总的运行时间
带参数多线程启动
'''
import time
import _thread as thread

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
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 两个参数，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ("yty", ))
    thread.start_new_thread(loop2, ("yty", "zr"))
    # time.sleep(6) 保证主进程不在子进程结束之前抛出
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 启动多线程后本线程作为主线程存在
    # 若主线程执行完毕，子线程可能会被中止
    while True:
        time.sleep(10)