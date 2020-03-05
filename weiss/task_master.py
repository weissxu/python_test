import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


# 自定义函数re_task_queue
def re_task_queue():
    global task_queue
    return task_queue


# 自定义函数re_result_queue
def re_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':
    manager = BaseManager(address=('', 5000), authkey=b'abc')

    manager.register('get_task_queue', callable=re_task_queue)
    manager.register('get_result_queue', callable=re_result_queue)

    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(5):
        n = random.randint(0, 10000)
        print('put task %d...' % n)
        task.put(n)

    print('try get results..')
    for i in range(5):
        r = result.get(timeout=30)
        print('result: %s' % r)

    manager.shutdown()
    print('master exit')


