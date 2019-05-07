import time
import threading

def loop1():
    print('Start loop1 at:', time.ctime())
    time.sleep(6)
    print('End loop1 at:', time.ctime())

def loop2():
    print('Start loop2 at:', time.ctime())
    time.sleep(1)
    print('End loop2 at:', time.ctime())

def loop3():
    print('Start loop3 at:', time.ctime())
    time.sleep(5)
    print('End loop3 at:', time.ctime())

def main():
    print('Starting at:', time.ctime())

    t1 = threading.Thread(target=loop1, args=( ))
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=( ))
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=( ))
    t3.setName("THR_3")
    t3.start()
    # 预计THR_2已结束
    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是： {0}".format(thr.getName()))

    print("正在运行的子线程数量为： {0}".format(threading.activeCount()))

    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 启动多线程后本线程作为主线程存在
    # 若主线程执行完毕，子线程可能会被中止
    while True:
        time.sleep(10)