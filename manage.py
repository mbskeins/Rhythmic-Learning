import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask

from app import app, db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    app.run()
