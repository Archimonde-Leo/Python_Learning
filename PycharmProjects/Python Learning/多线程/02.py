'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread

def loop1():
    print('Start loop1 at:', time.ctime())
    time.sleep(4)
    print('End loop1 at:', time.ctime())

def loop2():
    print('Start loop2 at:', time.ctime())
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def main():
    print('Starting at:', time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 两个参数，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    # time.sleep(6) 保证主进程不在子进程结束之前抛出
    print('All done at:', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)