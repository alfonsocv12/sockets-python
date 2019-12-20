import asyncio, websockets, json

class ClientController():

    def __init__(self):
        pass

    def send_notification(self, socket_id):
        '''
        Funcion encargada de mandar
        una notificacion al socket cuando algo se inserte
        '''
        asyncio.get_event_loop().run_until_complete(self.update_db(socket_id))

    async def update_db(self, socket_id):
        async with websockets.connect(
            "ws://localhost:5678/locationUpdate/{}".format(socket_id)
        ) as websocket:
            await websocket.send('listo')
            await websocket.close(1000, 'finish')
