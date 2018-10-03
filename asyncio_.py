import asyncio
import datetime
import random


async def my_sleep_func():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop):
    end_time = loop.time() + 10
    while True:
        print('Loop: {} Time: {}'.format(num, datetime.datetime.now()))
        if (loop.time() + 1) >= end_time:
            loop.close()
            break
        await my_sleep_func()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(display_date(1, loop))
    asyncio.ensure_future(display_date(2, loop))
    loop.run_forever()
    print('end_program')