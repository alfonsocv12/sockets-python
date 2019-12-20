import asyncio, websockets, json

async def db_change():
    uri = "ws://localhost:5678"
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.send("change")

asyncio.get_event_loop().run_until_complete(db_change())
