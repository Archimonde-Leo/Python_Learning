import threading
from time import sleep, ctime

loop = [4,2]

class ThreadFunc:

    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):

        print('Start loop', nloop, 'at ', ctime())
        sleep(nsec)
        print('End loop', nloop, 'at ', ctime())

def main():
    print("Starting at: ", ctime())
    # ThreadFunc(“loop”).loop
    # ==
    # t = ThreadFunc("loop")
    # t.loop
    t = ThreadFunc("loop")
    t1 = threading.Thread(target=t.loop, args=("LOOP1", 4))
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=("LOOP2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All done at: ", ctime())

if __name__ == '__main__':
    main()
