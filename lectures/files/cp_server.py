import asyncio
import websockets

async def consumer_handler(websocket):
    while True:
        message = await websocket.recv()
        # For each message received, pass it to the consumer coroutine
        await consumer(message)

# Producer handler
async def producer_handler(websocket):
    while True:
        # Wait for a message to be produced by the producer coroutine
        message = await producer()
        await websocket.send(message)

async def handler(websocket, path):
    # Create coroutines from the consumer and producer handler functions
    consumer_task = asyncio.ensure_future(consumer_handler(websocket))
    producer_task = asyncio.ensure_future(producer_handler(websocket))

    # Wait for any of these tasks to be completed
    # (One of them will terminate when the client disconnects)
    done, pending = await asyncio.wait(
        [consumer_task, producer_task],
        return_when=asyncio.FIRST_COMPLETED,  # Only need to wait until one of them terminates
    )

    # Cancel any task that is not yet terminated
    for task in pending:
        task.cancel()

total = 0

async def consumer(message):
    global total
    total += int(message)

async def producer():
    global total
    await asyncio.sleep(2)
    message = "Current total is {:d}".format(total)
    return message

start_server = websockets.serve(handler, 'localhost', 50001)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
