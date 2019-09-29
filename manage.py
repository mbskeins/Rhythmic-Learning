import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask

from app import app, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


if __name__ == '__main__':
    app.run()
