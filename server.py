import asyncio, datetime, random, websockets, json
from db_connection import db

locations = {}


def append_user(location_id, client_socket):
    '''
    Funcion encargada de agreagar un usuario
    '''
    location_2 = locations.get(location_id)\
        if locations.get(location_id) else create_new_location(location_id)
    if client_socket not in location_2:
        location_2.add(client_socket)


def create_new_location(location_id):
    '''
    Funcion encargada de crear un nuevo location
    '''
    locations[location_id] = set()
    return locations[location_id]


async def send_message(socket, path):
    '''
    Funcion encargada de mandar un mensaje
    '''
    await socket.send(db.table('location').get().to_json())


async def update_location(socket, path):
    '''
    Function dedicated to update_location to all users connected
    '''
    for send_to in locations.get(path.split('/')[2]):
        await send_to.send(db.table('location').get().to_json())


def set_path_action(socket, path):
    '''
    Funcion encargada de regresar la accion a
    ejecutar segun la ruta
    '''
    if "get_location" in path:
        append_user(
            path.split('/')[2],
            socket
        )
        return send_message
    else:
        return update_location


async def time(websocket, path):
    action = set_path_action(websocket, path)
    while True:
        await websocket.recv()
        await action(websocket, path)

start_server = websockets.serve(time, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
