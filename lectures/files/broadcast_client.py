import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

async def hello():
    async with websockets.connect('ws://localhost:50002') as websocket:
        while True:
            msg = await websocket.recv()
            print("Received: {}".format(msg))

asyncio.get_event_loop().run_until_complete(hello())
