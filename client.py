import asyncio, websockets, json

async def hello():
    uri = "ws://localhost:8765/sensor/758"
    async with websockets.connect(uri) as websocket:
        await websocket.send('give')
        while True:
            greeting = await websocket.recv()
            print(json.dumps(json.loads(greeting), indent=4))

asyncio.get_event_loop().run_until_complete(hello())
