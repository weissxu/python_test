import threading
import time


def loop():
    tname = threading.current_thread().name
    for i in range(5):
        print('thread %s is running %d' % (tname, i))
        time.sleep(1)

    print('thread %s ended.' % tname)


mname = threading.current_thread().name
print('thread %s is running.' % mname)

t = threading.Thread(target=loop)
t.start()
t.join()
print('thread %s ended' % mname)
print('==================')

balance = 0
lock=threading.Lock()

def change_id(n):
    global balance

    lock.acquire()
    try:
        balance += n
        balance -= n
    except:
        print("error")
    finally:
        lock.release()


def run_thread(n):
    for i in range(100000):
        change_id(n)


t1 = threading.Thread(target=run_thread, args={5, })
t2 = threading.Thread(target=run_thread, args={8, })
t3 = threading.Thread(target=run_thread, args={10, })

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(balance)
