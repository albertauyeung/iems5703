import asyncio
import websockets
import random

async def hello():
    async with websockets.connect('ws://localhost:50001') as websocket:
        i = random.randint(1, 20)
        print("Number sent: {:d}".format(i))
        await websocket.send(str(i))
        while True:
            msg = await websocket.recv()
            print("{}".format(msg))

asyncio.get_event_loop().run_until_complete(hello())
