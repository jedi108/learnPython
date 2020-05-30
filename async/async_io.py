# * Сначала мы объявили пару простейших корутин, которые притворяются неблокирующими, используя sleep из asyncio
# * Корутины могут быть запущены только из другой корутины, или обёрнуты в задачу с помощью create_task
# * После того, как у нас оказались 2 задачи, объединим их, используя wait
# * И, наконец, отправим на выполнение в цикл событий через run_until_complete

import asyncio


async def foo():
    print("start foo")
    await asyncio.sleep(0)
    print("switch to foo again")


async def bar():
    print("start bar")
    await asyncio.sleep(0)
    print("switch to foo bar")

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()