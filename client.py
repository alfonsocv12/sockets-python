import asyncio, websockets, json

async def hello():
    uri = "ws://localhost:5678/get_location/12"
    async with websockets.connect(uri) as websocket:
        await websocket.send('give')
        while True:
            greeting = await websocket.recv()
            print(json.dumps(json.loads(greeting), indent=4))

asyncio.get_event_loop().run_until_complete(hello())
