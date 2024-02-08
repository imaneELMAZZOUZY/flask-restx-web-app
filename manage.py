import os
import unittest

from flask.cli import FlaskGroup
from app.main import create_app, db
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()





from app.main.model import user
from app.main.model import blacklist

if __name__ == '__main__':
   app.run()
 
