import queue
import time
from multiprocessing.managers import BaseManager

manager = BaseManager(address=('localhost', 5000), authkey=b'abc')
manager.register('get_task_queue')
manager.register('get_result_queue')

manager.connect()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(5):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Queue.Empty:
        print('task queue is empty')
print('work exit..')

exit()
