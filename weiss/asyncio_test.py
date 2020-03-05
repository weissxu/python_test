import asyncio
import threading
from datetime import datetime


async def hello():
    print('hello,world！（%s,%s）' % (threading.currentThread(),datetime.now()))
    await asyncio.sleep(1)
    print('hello again!(%s,%s）' % (threading.currentThread(),datetime.now()))


loop = asyncio.get_event_loop()
task = [hello(), hello()]
loop.run_until_complete(asyncio.wait(task))
loop.close()
