from bottle import route, run, template, request, response
from db_connection import db
from controllers.client_controller import ClientController
from models.location_model import LocationModel

client_controller = ClientController()

@route('/insert', method='GET')
def index():
    response.content_type = 'application/json'
    location = LocationModel()
    location.pivot_id = 12
    location.polilinea = request.json.get('line')
    location.save()
    client_controller.send_notification(location.pivot_id)
    return {'msg': 'listo'}

run(host='localhost', port=8080)
