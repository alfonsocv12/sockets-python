from orator import Model

class LocationModel(Model):

    __table__ = 'location'
    __connection__ = 'local'
    __fillable__ = ['pivot_id', 'polilinea']
    __hidden__ = ['id']
    __timestamps__ = False
