import asyncio
import time

async def fake_io_operation():
    print("Perform I/O now...")
    await asyncio.sleep(1)
    print("I/O completed")

async def compute_square(x):
    print("Compute square of %d" % x)
    await fake_io_operation()
    print("%d" % (x * x))

loop = asyncio.get_event_loop()
tasks = []
for i in [4, 5, 6, 7]:
    tasks.append(asyncio.ensure_future(compute_square(i)))

loop.run_until_complete(asyncio.wait(tasks))
loop.close()

