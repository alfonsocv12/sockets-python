import sys
from env import os
from orator import DatabaseManager, Model

try:
    db = DatabaseManager(os.environ.get('connexion'))
    Model.set_connection_resolver(db)
except Exception:
    e = sys.exc_info()[0]
    sys.stdout.write('Got error {!r}, error is {0}'.format(e, e.args[0]))
