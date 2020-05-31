import asyncio
from collections import deque

not_stop_app = True
q = deque()


async def put():
    global not_stop_app
    for i in range(1, 10):
        q.append(i)
        await asyncio.sleep(0)
    await asyncio.sleep(0)
    not_stop_app = False


async def pop():
    while not_stop_app:
        if len(list(q)) >= 1:
            el = q.popleft()
            print(el)
        await asyncio.sleep(0)

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(put()), ioloop.create_task(pop())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()