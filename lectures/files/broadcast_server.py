import asyncio
import functools
import websockets
from websockets.exceptions import ConnectionClosed

clients = set()

async def broadcast_message(clients):
    while True:
        print("Number of clients: {:d}".format(len(clients)))
        for c in clients:
            await c.send("Hello!")
        await asyncio.sleep(3)

async def handle(websocket, path, clients):
    print("Client {} connected".format(str(websocket.remote_address)))
    clients.add(websocket)
    while True:
        try:
            await websocket.recv()
        except ConnectionClosed as ex:
            print("Client disconnected")
        finally:
            clients.remove(websocket)
            break

broadcast_coroutine = asyncio.ensure_future(broadcast_message(clients))
handler = functools.partial(handle, clients=clients)
start_server = websockets.serve(handler, 'localhost', 50002)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([start_server, broadcast_coroutine]))
loop.run_forever()
